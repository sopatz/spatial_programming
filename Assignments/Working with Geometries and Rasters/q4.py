# Lab 6 Question 4
import arcpy
import fileinput
arcpy.env.overwriteOutput = True
wkspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'
arcpy.env.workspace = wkspace

new_pgfc = "bh_fire"
arcpy.management.CreateFeatureclass(wkspace, new_pgfc, "Polygon", spatial_reference = "streams")
infile = "C:/PythonPro/Exercise06/Lab06Data/fireperim.txt"
with arcpy.da.InsertCursor(new_pgfc, ["SHAPE@"]) as cursor:
    array = arcpy.Array()
    for line in fileinput.input(infile):
        ID, X, Y = line.split()
        array.add(arcpy.Point(X, Y))
    cursor.insertRow([arcpy.Polygon(array)])
    fileinput.close()

fc = "bh_fire"
vertices = 0
perimeter = 0
area = 0
with arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@", "SHAPE@LENGTH", "SHAPE@AREA"]) as cursor:
    for row in cursor:
        for point in row[1].getPart(0):
            vertices += 1
        perimeter += row[2]
        area += row[3]

desc = arcpy.da.Describe(fc)
units = desc["spatialReference"].linearUnitName

print(f"The Black Hills fire polygon has {vertices} vertices, a perimeter of {perimeter} {units}s, and covers {area} {units}s squared of area.")

