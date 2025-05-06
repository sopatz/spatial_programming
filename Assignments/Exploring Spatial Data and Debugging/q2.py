# Lab 4 Question 2

import arcpy
arcpy.env.workspace = "C:/PythonPro/Exercise04/New Mexico.gdb"
fclist = arcpy.ListFeatureClasses()
for dataset in fclist:
    description = arcpy.da.Describe(dataset)
    name = description["baseName"]
    data_type = description["dataType"]
    shape_type = description["shapeType"]
    coord_sys = description["spatialReference"].name
    print(f"{name} is a {shape_type} {data_type} in the {coord_sys} coordinate system.")
