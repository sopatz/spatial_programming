# Question 5

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

tracts_geology_Intersect = arcpy.analysis.Intersect(
    in_features="tracts_austin #;geology_austin #",
    out_feature_class="tracts_geology_Intersect",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="INPUT"
)

tract_geo_selection = arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=tracts_geology_Intersect,
    selection_type="NEW_SELECTION",
    where_clause="POP_SQMI < 1000 And UNIT_NAME LIKE '%Limestone%'",
    invert_where_clause=None
)

# Copy selected features to new feature class
arcpy.management.CopyFeatures(tract_geo_selection, "rural_septic")


