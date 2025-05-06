# Lab 4 Question 3

import arcpy
arcpy.env.workspace = "C:/PythonPro/Exercise04/New Mexico.gdb"
fieldlist = arcpy.ListFields("counties")
for field in fieldlist:
    print(field.name + " (" + field.type + ")")
