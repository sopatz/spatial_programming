# Lab 5 Question 8
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

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

