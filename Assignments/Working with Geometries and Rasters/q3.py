# Lab 6 Question 3
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'

fc = "streams"
with arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"]) as cursor:
    all_streams = []
    for row in cursor:
        all_streams.append(row[0])
    all_streams.sort(reverse=True)
    print("The lengths of the 5 longest streams are:")
    for strm in all_streams[0:5]:
        print(f"{strm} meters")




