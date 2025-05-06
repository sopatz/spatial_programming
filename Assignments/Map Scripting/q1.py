# Lab 7 Question 1
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise07'

prj = arcpy.mp.ArcGISProject("Exercise07.aprx")
maps = prj.listMaps()
for map in maps:
    print("Map: " + map.name)
    print("Units: " + map.mapUnits)
    print("Coordinate System: " + map.spatialReference.name + '\n')
