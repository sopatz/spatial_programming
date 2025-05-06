# Lab 6 Question 2
import arcpy
import os
arcpy.env.overwriteOutput = True
wkspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'
data_folder = 'C:/PythonPro/Exercise06/Lab06Data'
arcpy.env.workspace = data_folder
raster_list = arcpy.ListRasters()
for rastr in raster_list:
    rastr_name = arcpy.da.Describe(rastr)["baseName"]
    new_rastr = os.path.join(wkspace, rastr_name)
    arcpy.management.CopyRaster(rastr, new_rastr)

# Print: Name, format, compression, # of bands, coordinate system.
arcpy.env.workspace = wkspace
bh_rast = arcpy.ListRasters()
for rastr in bh_rast:
    desc = arcpy.da.Describe(rastr)
    print("Raster Name: " + desc["baseName"])
    print("Format: " + desc["format"])
    print("Compression: " + desc["compressionType"])
    print("Number of Bands: " + str(desc["bandCount"]))
    print("Coordinate System: " + desc["spatialReference"].name + '\n')

