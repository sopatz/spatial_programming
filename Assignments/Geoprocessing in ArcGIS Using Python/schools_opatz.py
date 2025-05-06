# Question 7

import arcpy
arcpy.env.workspace = "C:\PythonPro\Exercise03\Exercise03.gdb"

limestone = arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="geology_austin",
    selection_type="NEW_SELECTION",
    where_clause="UNIT_NAME LIKE '%Limestone%'",
    invert_where_clause=None
)

arcpy.analysis.Buffer(
    in_features="creeks_austin",
    out_feature_class="creeks_buffer",
    buffer_distance_or_field="1000 Feet",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="ALL",
    dissolve_field=None,
    method="PLANAR"
)

arcpy.analysis.Intersect(
    in_features=[limestone, "creeks_buffer"],
    out_feature_class="limestone_creek_intersect",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="INPUT"
)

arcpy.analysis.Intersect(
    in_features="schools_austin #; limestone_creek_intersect #",
    out_feature_class="schools_meeting_criteria",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="INPUT"
)

school_count = arcpy.management.GetCount('schools_meeting_criteria')
print(f"There are {school_count} schools in Austin that are in close proximity to creeks and built on limestone.")
