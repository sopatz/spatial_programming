# Lab 5 Question 3
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

print(f"There are {arcpy.management.GetCount('airports_wa')} airports in Washington.")
print(f"There are {arcpy.management.GetCount('amtrak_stations_wa')} amtrak stations in Washington.")
print(f"There are {arcpy.management.GetCount('cities_wa')} cities in Washington.")
print(f"There are {arcpy.management.GetCount('states_wa')} states in Washington. Itself!")

