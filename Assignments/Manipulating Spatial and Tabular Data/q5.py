# Lab 5 Question 5
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

fc = "amtrak_stations_wa"
with arcpy.da.UpdateCursor(fc, ["stntype"]) as cursor:
    for row in cursor:
        if row[0] == 'BUS':
            cursor.deleteRow()

