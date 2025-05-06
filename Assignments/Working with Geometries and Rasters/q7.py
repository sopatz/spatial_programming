# Lab 6 Question 7
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'

outraster = arcpy.sa.Slope("topo")
outraster.save("slope")

outraster = arcpy.sa.Viewshed(
    in_raster="topo",
    in_observer_features="towers",
    z_factor=1,
    curvature_correction="FLAT_EARTH",
    refractivity_coefficient=0.13,
    out_agl_raster=None
)
outraster.save("tower_view")

