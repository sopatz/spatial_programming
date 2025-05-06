# Lab 5 Question 1

import arcpy
import os
arcpy.env.overwriteOutput = True
wkspace = 'C:/PythonPro/Exercise05'
data_folder = 'C:/PythonPro/Exercise05/Lab05Data'
new_gdb = 'PacificNW.gdb'
arcpy.CreateFileGDB_management(wkspace, new_gdb)
arcpy.env.workspace = data_folder
ftr_classes = arcpy.ListFeatureClasses() #get all feature classes in Lab05Data folder
for fc in ftr_classes:
    fc_name = arcpy.da.Describe(fc)["baseName"]
    new_fc = os.path.join(wkspace, new_gdb, fc_name) #copy paths to new gdb
    arcpy.CopyFeatures_management(fc, new_fc) #copy features to new gdb

#Print all feature classes in "PacificNW.gdb"
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'
pac_fc = arcpy.ListFeatureClasses()
print("Feature classes in \"PacificNW\": ")
for fc in pac_fc:
    print(fc)
