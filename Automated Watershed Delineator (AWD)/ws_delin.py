# Automated Watershed Delineation from DEM Raster File
# Spatial Programming Final Project
# Spring 2025 Spatial Programming (GEOG-59076), Kent State University
# Seth Opatz
# 05/04/2025

import arcpy
import os
import tempfile
arcpy.env.overwriteOutput = True
arcpy.env.workspace = None

# Make sure no intermittent files get saved to output folder
arcpy.env.scratchWorkspace = tempfile.gettempdir()

r"""
=======================================================================================
If you want to test the program:
Download this DEM (can use other DEM if you wish):
https://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/2000.02.11/N40W082.SRTMGL1.hgt.zip

Make a project in ArcGIS Pro called "SP_FinalProject" in the C:\PythonPro directory

Put the DEM (N40W082.hgt) in the newly created project directory

File path to DEM raster:
C:\PythonPro\SP_FinalProject\N40W082.hgt

Directory path to send output(s):
C:\PythonPro\SP_FinalProject\SP_FinalProject.gdb
=======================================================================================
"""

# Get file path to DEM from user
while True:
    # Ask user for DEM file path
    dem = input("File path to DEM raster: ")
    # File does not exist
    if not os.path.exists(dem):
        print("File path does not exist. Please try again.")
    else: # File exists
        try:
            desc = arcpy.Describe(dem)
            # Check to make sure input file is a raster
            if desc.dataType not in ["RasterDataset", "RasterLayer"]:
                print("This file is not a valid raster dataset. Please input a valid raster.")
            else:
                break  # It's a valid raster
        except Exception as e:
            print(f"Error reading raster: {e}")

# Get file path to send output(s) from user
while True:
    # Ask user for path to desired output directory
    output_location = input("Directory path to send output(s): ")
    # Path does not exist
    if not os.path.exists(output_location):
        print("Directory path does not exist. Please try again.")
    # Path is not a directory
    elif not os.path.isdir(output_location):
        print("This is not a directory. Please input a valid directory path.")
    # Path does not have write privileges
    elif not os.access(output_location, os.W_OK):
        print("You do not have write permission to this directory. Please choose a different one.")
    else: break # Directory is valid

# Ask user what output(s) they want (polygons, raster, or both) and save their choice
while True:
    output_choice = input("Do you want watershed (p)olygons, (r)aster, or (b)oth? ")
    if output_choice == 'p' or output_choice == 'r' or output_choice == 'b':
        break # Valid character entered
    print("Invalid choice. Please input 'p', 'r', or 'b'.")

# Ask user for flow accumulation threshold so they can choose their desired watershed size
while True:
    acc_threshold = input("Set flow accumulation threshold (smaller number = more watersheds, larger number = less watersheds): ")
    try:
        value = int(acc_threshold)
        if value > 0:
            break # Flow accumulation threshold is valid
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Not a valid number. Please enter a positive integer.")

# Fill DEM to smooth out any imperfections in the data
print("\nFilling DEM...")
filled_dem = arcpy.sa.Fill(
    in_surface_raster=dem,
    z_limit=None
)

# Use filled DEM to calculate 8-direction flow direction raster
print("Calculating Flow Direction...")
flow_dir = arcpy.sa.FlowDirection(
    in_surface_raster=filled_dem,
    force_flow="NORMAL",
    out_drop_raster=None,
    flow_direction_type="D8"
)

# Calculates flow accumulation for each pixel using the flow direction raster
print("Calculating Flow Accumulation...")
flow_acc = arcpy.sa.FlowAccumulation(
    in_flow_direction_raster=flow_dir,
    in_weight_raster=None,
    data_type="FLOAT",
    flow_direction_type="D8"
)

# Extract pixels whose flow accumulation value is more than the threshold the user input
print("Extracting Streams...")
expr = "VALUE > " + acc_threshold
streams_temp = arcpy.sa.Con(flow_acc, 1, 0, expr)

# Transform non-stream pixels into NODATA, leaving only stream pixels
print("Reclassifying Streams...")
streams = arcpy.sa.Reclassify(
    in_raster=streams_temp,
    reclass_field="Value",
    remap="0 NODATA",
    missing_values="DATA"
)

# Give each stream section between intersections a unique ID
print("Assigning IDs to Stream Segments...")
strm_link = arcpy.sa.StreamLink(
    in_stream_raster=streams,
    in_flow_direction_raster=flow_dir
)

# Use stream link IDs to delineate watersheds
print("Delineating Watersheds...")
watersheds_raster = arcpy.sa.Watershed(
    in_flow_direction_raster=flow_dir,
    in_pour_point_data=strm_link,
    pour_point_field="Value"
)
# Output watershed raster if the user chose to do so
if output_choice == 'r' or output_choice == 'b':
    # Get base name of DEM without extension
    dem_basename = os.path.splitext(os.path.basename(dem))[0]

    if output_location.lower().endswith(".gdb"):
        base_output_name = f"{dem_basename}_watersheds"
        wr_path = os.path.join(output_location, base_output_name)
        if arcpy.Exists(wr_path):
            arcpy.management.Delete(wr_path)
    else:
        base_output_name = f"{dem_basename}_watersheds.tif"
        wr_path = os.path.join(output_location, base_output_name)
        if os.path.exists(wr_path):
            os.remove(wr_path)

    # Save watershed raster
    watersheds_raster.save(wr_path)
    print(f"Saved watershed raster to: {wr_path}")


# Convert watershed raster to polygons and output it if the user chose to do so
if output_choice in ['p', 'b']:
    print("Converting Watersheds Raster to Polygons...")
    ws_name = f"{dem_basename}_watersheds_poly"
    ws_path = os.path.join(output_location, ws_name)
    if arcpy.Exists(ws_path):
        arcpy.management.Delete(ws_path)
    # Run the Raster to Polygon tool in arcpy.sa
    arcpy.conversion.RasterToPolygon(
        in_raster=watersheds_raster,
        out_polygon_features=ws_path,
        simplify="SIMPLIFY",
        raster_field="Value",
        create_multipart_features="SINGLE_OUTER_PART",
        max_vertices_per_feature=None
    )
    print(f"Saved watershed polygons to: {ws_path}")

