# Lab 5 Question 2
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise05/PacificNW.gdb'

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
