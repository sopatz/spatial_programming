# Lab 5 Question 6
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

cities = []
fc = "amtrak_stations_wa"
cursor = arcpy.da.SearchCursor(fc, ["city"], sql_clause=(None, "ORDER BY city ASC"))
for row in cursor:
    cities.append(row[0])

print("Each city in Washington with an amtrak station (listed alphabetically):")
for city in cities:
    print(city)

print("\nLast 5 cities in Washington alphabetically with an amtrak station:")
print(cities[-5:])


    


