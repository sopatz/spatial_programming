# Lab 6 Question 8 (Challenge)
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'

# Get the fire perimeter geometry from the 'bh_fire' polygon
with arcpy.da.SearchCursor("bh_fire", ["SHAPE@"]) as fc_cursor:
    fire_geom = next(fc_cursor)[0]

# Get units from spatial reference for printing purposes later
desc = arcpy.da.Describe("towers")
units = desc["spatialReference"].linearUnitName

# Loop through towers and measure distance
with arcpy.da.SearchCursor("towers", ["OID@", "SHAPE@", "NAME"]) as tower_cursor:
    for row in tower_cursor:
        oid = row[0]
        tower_geom = row[1]
        distance = tower_geom.distanceTo(fire_geom)
        print(f"The {row[2]} tower is {distance:.3f} {units}s from the fire perimeter")

