# Question 6

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

road_soils_Intersect = arcpy.analysis.Intersect(
    in_features="majroads_austin #;soils_austin #",
    out_feature_class="roads_soils_Intersect",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="INPUT"
)

roads_on_clay = arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=road_soils_Intersect,
    selection_type="NEW_SELECTION",
    where_clause="CLAY > 50",
    invert_where_clause=None
)

# Add new field converting feet length to mile length
arcpy.management.AddField(roads_on_clay, "Mileage", "DOUBLE")

factor = 0.0001893939 #conversion factor for feet to miles

# Calculate the adjusted values using an Update Cursor
with arcpy.da.UpdateCursor(roads_on_clay, ["Shape_Length", "Mileage"]) as cursor:
    for row in cursor:
        row[1] = row[0] * factor  # Multiply Shape_Length by factor
        cursor.updateRow(row)

# Copy selected features to new feature class
arcpy.management.CopyFeatures(roads_on_clay, "roads_at_risk")

arcpy.analysis.Statistics(
    "roads_at_risk",
    'risk_roadway_mileage',
    [["Mileage", "SUM"]]
)
