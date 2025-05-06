# Question 2

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

count = arcpy.management.GetCount('watersheds_austin')
print(f"There are {count} watersheds in Austin.")

arcpy.analysis.Statistics('tracts_austin',
                          'total_pop_austin',
                          [["POP2010", "SUM"], ["POP2014", "SUM"]])
