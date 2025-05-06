# Lab 5 Question 4
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

fc = "airports_wa"
sql_exp = '"PASSENGERS" > 100000'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
print("Airports in Washington with more than 100,000 passengers:")
for row in cursor:
    print(row[0])

fc = "cities_wa"
sql_exp = '"POPULATION" > 100000'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
print("\nCities in Washington with more than 100,000 population in 2014:")
for row in cursor:
    print(row[0])

fc = "airports_wa"
sql_exp = '"FACILITY" = \'Ultralight\''
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
print("\nAirports in Washington for ultralight vehicles:")
for row in cursor:
    print(row[0])


