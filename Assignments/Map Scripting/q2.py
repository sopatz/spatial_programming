# Lab 7 Question 2
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise07'

prj = arcpy.mp.ArcGISProject("Exercise07.aprx")
maps = prj.listMaps()
for map in maps:
    print("Map: " + map.name)
    layers = map.listLayers()
    for layer in layers:
        if layer.isFeatureLayer:
            print(layer.name + " is a feature layer")
        elif layer.isBasemapLayer:
            print(layer.name + " is a basemap layer")
        elif layer.isRasterLayer:
            print(layer.name + " is a raster layer")
        else: print(layer.name + "is none of the types accounted for.")
    print() #Skip a line for visual clarity
