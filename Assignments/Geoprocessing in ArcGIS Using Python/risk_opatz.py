# Question 3

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

# Select all wells within 1000 feet of a creek
wells_at_risk = arcpy.management.SelectLayerByLocation("wells_austin",
                                       "WITHIN_A_DISTANCE",
                                       "creeks_austin",
                                       "1000 feet")

# Copy selected features to new feature class
arcpy.management.CopyFeatures(wells_at_risk, "wells_at_risk")
