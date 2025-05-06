# Lab 4 Question 1

import arcpy
import os
arcpy.env.overwriteOutput = True
wkspace = "C:/PythonPro/Exercise04"
data_folder = "C:/PythonPro/Exercise04/Lab04Data"
new_gdb = "New Mexico.gdb"
arcpy.CreateFileGDB_management(wkspace, new_gdb)
arcpy.env.workspace = data_folder
ftr_classes = arcpy.ListFeatureClasses() #get all feature classes in Lab04Data folder
for fc in ftr_classes:
    fc_name = arcpy.da.Describe(fc)["baseName"]
    new_fc = os.path.join(wkspace, new_gdb, fc_name) #copy paths to new gdb
    arcpy.CopyFeatures_management(fc, new_fc) #copy features to new gdb

#Print all feature classes in "New Mexico.gdb"
arcpy.env.workspace = "C:/PythonPro/Exercise04/New Mexico.gdb"
nm_fc = arcpy.ListFeatureClasses()
print("Feature classes in \"New Mexico.gdb\": ")
for fc in nm_fc:
    print(fc)
