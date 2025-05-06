# Question 1

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

features = ["creeks", "geology", "majroads", "schools", "soils", "tracts", "watersheds", "wells"]

for item in features:
    arcpy.analysis.Clip(item, "austin_bnd", item + "_austin") #concatenate feature name string to output file name string
