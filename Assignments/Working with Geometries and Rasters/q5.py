# Lab 6 Question 5
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'

min_elev = arcpy.management.GetRasterProperties("topo", "MINIMUM")
max_elev = arcpy.management.GetRasterProperties("topo", "MAXIMUM")
desc = arcpy.da.Describe('topo')
units = desc['spatialReference'].linearUnitName
print(f"The black hills field site ranges from {min_elev} {units}s to {max_elev} {units}s.") 

