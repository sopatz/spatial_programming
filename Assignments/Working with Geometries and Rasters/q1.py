# Lab 6 Question 1
import arcpy
import os
arcpy.env.overwriteOutput = True
wkspace = 'C:/PythonPro/Exercise06'
data_folder = 'C:/PythonPro/Exercise06/Lab06Data'
new_gdb = 'BlackHills.gdb'
arcpy.CreateFileGDB_management(wkspace, new_gdb)
arcpy.env.workspace = data_folder
ftr_classes = arcpy.ListFeatureClasses()
for fc in ftr_classes:
    fc_name = arcpy.da.Describe(fc)["baseName"]
    new_fc = os.path.join(wkspace, new_gdb, fc_name) #copy paths to new gdb
    arcpy.CopyFeatures_management(fc, new_fc) #copy features to new gdb

#Print all feature classes in "BlackHills.gdb"
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'
bh_fc = arcpy.ListFeatureClasses()
print("Feature classes in \"BlackHills\": ")
for fc in bh_fc:
    print(fc)
