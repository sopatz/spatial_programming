# Lab 5 All Scripts (Questions 1-8 combined)

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


# Lab 5 Question 2
in_fc = 'cities'
out_fc = 'cities_wa'
delim_field = arcpy.AddFieldDelimiters(in_fc, "ST")
sql_exp = delim_field + " = 'WA'"
arcpy.analysis.Select(in_fc, out_fc, sql_exp)

in_fc = 'airports'
out_fc = 'airports_wa'
delim_field = arcpy.AddFieldDelimiters(in_fc, "STATE")
sql_exp = delim_field + " = 'WA'"
arcpy.analysis.Select(in_fc, out_fc, sql_exp)

in_fc = 'amtrak_stations'
out_fc = 'amtrak_stations_wa'
delim_field = arcpy.AddFieldDelimiters(in_fc, "STATE")
sql_exp = delim_field + " = 'WA'"
arcpy.analysis.Select(in_fc, out_fc, sql_exp)

in_fc = 'states'
out_fc = 'states_wa'
delim_field = arcpy.AddFieldDelimiters(in_fc, "STATE_ABBR")
sql_exp = delim_field + " = 'WA'"
arcpy.analysis.Select(in_fc, out_fc, sql_exp)


# Lab 5 Question 3
print(f"\nThere are {arcpy.management.GetCount('airports_wa')} airports in Washington.")
print(f"There are {arcpy.management.GetCount('amtrak_stations_wa')} amtrak stations in Washington.")
print(f"There are {arcpy.management.GetCount('cities_wa')} cities in Washington.")
print(f"There are {arcpy.management.GetCount('states_wa')} states in Washington. Itself!")


# Lab 5 Question 4
fc = "airports_wa"
sql_exp = '"PASSENGERS" > 100000'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
print("\nAirports in Washington with more than 100,000 passengers:")
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


# Lab 5 Question 5
fc = "amtrak_stations_wa"
with arcpy.da.UpdateCursor(fc, ["stntype"]) as cursor:
    for row in cursor:
        if row[0] == 'BUS':
            cursor.deleteRow()


# Lab 5 Question 6
cities = []
fc = "amtrak_stations_wa"
cursor = arcpy.da.SearchCursor(fc, ["city"], sql_clause=(None, "ORDER BY city ASC"))
for row in cursor:
    cities.append(row[0])

print("\nEach city in Washington with an amtrak station (listed alphabetically):")
for city in cities:
    print(city)

print("\nLast 5 cities in Washington alphabetically with an amtrak station:")
print(f"{cities[-5:]}\n")


# Lab 5 Question 7
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


# Lab 5 Question 8
fc = "cities_wa"
new_field = "pop_change"
fieldtype = "LONG"
pop_change = arcpy.ValidateFieldName(new_field)
arcpy.management.AddField(fc, pop_change, fieldtype)

arcpy.management.CalculateField(
    in_table="cities_wa",
    field="pop_change",
    expression="!POPULATION! - !POP2010!",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

sql_exp = '"pop_change" < 0'
cursor = arcpy.da.SearchCursor(fc, ["NAME", "pop_change"], sql_exp)
print("\nCities in Washington that lost population from 2010 to 2014:")
for row in cursor:
    print(f"{row[0]}'s population declined by {-row[1]} people between 2010 and 2014")




