# Lab 7 Question 5
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise07'

prj = arcpy.mp.ArcGISProject("Exercise07_q4.aprx")
lc_map = prj.listMaps("Landcover")[0]

cities = lc_map.listLayers("cities")[0]
lc_map.removeLayer(cities)
wi = lc_map.listLayers("World Imagery")[0]
lc_map.removeLayer(wi)

lc_remap = arcpy.sa.RemapValue([
    #Forest: (includes evergreen, deciduous, mixed, transitional) green
    [29, 1], [31, 1], [39, 1], [71, 1], [32, 1], [33, 1], [34, 1], [35, 1], [36, 1], [37, 1],
    [38, 1], [41, 1], [42, 1], [44, 1], [45, 1], [46, 1], [47, 1], [48, 1], [49, 1], [50, 1],
    [51, 1], [52, 1], [53, 1], [54, 1], [55, 1], [56, 1], [57, 1], [58, 1], [59, 1], [60, 1],
    [61, 1], [62, 1], [63, 1], [64, 1], [65, 1], [66, 1], [67, 1], [30, 1], [40, 1], [68, 1],
    [69, 1], [73, 1], [110, 1], [113, 1], [123, 1], [124, 1], [126, 1], [127, 1], [129, 1],
    [130, 1], [131, 1], [133, 1], [150, 1], [118, 1], [119, 1], [120, 1], [121, 1],
    
    #Barren: (includes ash, dune, rock) purple
    [26, 2], [115, 2], [116, 2], [117, 2], [21, 2], [22, 2], [27, 2], [15, 2], [18, 2], [28, 2],
    [78, 2], [122, 2], [12, 2], [13, 2], [14, 2], [16, 2], [17, 2], [19, 2], [20, 2], [24, 2],
    [25, 2], [72, 2], [107, 2],
    
    #Water: Blue
    [1, 3], [136, 3],
    
    #Wetlands: dark green
    [137, 4], [138, 4], [139, 4], [142, 4], [144, 4], [147, 4], [149, 4], [114, 4], [125, 4], [132, 4],
    [134, 4], [128, 4], [140, 4], [141, 4],
    
    #Built-up: (urban, developed, residential) red
    [5, 5], [4, 5], [3, 5], [6, 5],
    
    #Agriculture: (agriculture, crops, pasture) yellow
    [10, 6], [2, 6], [8, 6], [11, 6], [9, 6], 
    
    #Brush: (grasslands, shrublands, steppe) tan
    [111, 7], [112, 7], [84, 7], [89, 7], [98, 7], [104, 7], [23, 7], [75, 7], [86, 7], [94, 7],
    [95, 7], [96, 7], [97, 7], [99, 7], [100, 7], [101, 7], [102, 7], [103, 7], [105, 7], [106, 7],
    [108, 7], [135, 7], [145, 7], [146, 7], [77, 7], [74, 7], [76, 7], [90, 7], [91, 7], [92, 7],
    [148, 7], [43, 7], [70, 7], [79, 7], [80, 7], [81, 7], [82, 7], [83, 7], [85, 7], [87, 7],
    [88, 7], [93, 7]
    
])

out_recl = arcpy.sa.Reclassify('Exercise07.gdb/landcover', 'Value', lc_remap, 'NODATA')
out_recl.save("Exercise07.gdb/lc_reclass")
lc_map.addDataFromPath('C:/PythonPro/Exercise07/Exercise07.gdb/lc_reclass')

lc = lc_map.listLayers("lc_reclass")[0]
sym = lc.symbology
sym.updateColorizer('RasterUniqueValueColorizer')
sym.colorizer.field = "Value"

label_dict = {
    '1': 'Forest',
    '2': 'Barren',
    '3': 'Water',
    '4': 'Wetlands',
    '5': 'Urban',
    '6': 'Cropland',
    '7': 'Grassland'
}

for group in sym.colorizer.groups:
    for item in group.items:
        val = str(item.values[0])
        if val in label_dict:
            item.label = label_dict[val]
            if val == '1':
                item.color = {'RGB': [34, 139, 34, 100]}
            elif val == '2':
                item.color = {'RGB': [160, 32, 240, 100]}
            elif val == '3':
                item.color = {'RGB': [0, 0, 255, 100]}
            elif val == '4':
                item.color = {'RGB': [0, 100, 0, 100]}
            elif val == '5':
                item.color = {'RGB': [255, 0, 0, 100]}
            elif val == '6':
                item.color = {'RGB': [255, 255, 0, 100]}
            elif val == '7':
                item.color = {'RGB': [210, 180, 140, 100]}
lc.symbology = sym

prj.saveACopy("Exercise07_q5.aprx")
del prj


