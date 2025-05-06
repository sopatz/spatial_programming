# Question 4

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

# Select moderate flood risk soils
mfr_soils = arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="soils_austin",
    selection_type="NEW_SELECTION",
    where_clause="AFLDFREQ < 3"
)

# Select schools that intersect the moderate flood risk soils
schools_at_risk = arcpy.management.SelectLayerByLocation(
    in_layer="schools_austin",
    overlap_type="INTERSECT",
    select_features = mfr_soils
)

# Copy selected features to new feature class
arcpy.management.CopyFeatures(schools_at_risk, "schools_at_risk")
