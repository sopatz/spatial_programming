# Lab 6 Question 6
import arcpy
import numpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise06/BlackHills.gdb'

lc_remap = arcpy.sa.RemapValue([
    [11, 1], [90, 1], [95, 1],
    [21, 2], [22, 2], [23, 2], [24, 2],
    [41, 3], [42, 3], [43, 3],
    [52, 4], [71, 4], [81, 4], [82, 4],
    [31, 5]
])
out_recl = arcpy.sa.Reclassify('landcover', 'Value', lc_remap, 'NODATA')
out_recl.save("landcover_reclass")

r = arcpy.Raster("landcover_reclass")

# Convert raster to NumPy array
arr = arcpy.RasterToNumPyArray(r)

# Get cell size
cell_area = r.meanCellWidth * r.meanCellHeight

# Count pixels per class
unique, counts = numpy.unique(arr, return_counts=True)

desc = arcpy.da.Describe("landcover_reclass")
unit = desc['spatialReference'].linearUnitName

# Print area for each class
for val, count in zip(unique, counts):
    if val == 0: continue #skip to next loop iteration
    area = count * cell_area
    print(f"Class {val}: {area} square {unit}s")


