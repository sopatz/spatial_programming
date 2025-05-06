# Lab 5 Question 7
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

fc = "cities_wa"
delim_field = arcpy.AddFieldDelimiters(fc, "POPULATION")
sql_exp = delim_field + " > 100000"
with arcpy.da.UpdateCursor(fc, ["CLASS"], sql_exp) as cursor:
    for row in cursor:
        row[0] = "major city"
        cursor.updateRow(row)

cursor = arcpy.da.SearchCursor(fc, ["NAME", "CLASS", "POPULATION"], sql_clause=(None, "ORDER BY POPULATION DESC"))
for i, row in enumerate(cursor):
    if i >= 10:
        break
    print(f"{row[0]} is a {row[1]} with a population of {row[2]}")


