# Lab 4 Question 4

import arcpy
arcpy.env.workspace = "C:/PythonPro/Exercise04/New Mexico.gdb"
feature_count = arcpy.management.GetCount("cities")
print(f"The cities feature class has {feature_count} features.")
