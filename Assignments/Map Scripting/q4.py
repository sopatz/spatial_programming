# Lab 7 Question 4
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise07'

prj = arcpy.mp.ArcGISProject("Exercise07_q3.aprx")
pop_map = prj.listMaps("Population")[0]
pop_map.addBasemap("Terrain with Labels")

#Remove labels from basemap
labels = pop_map.listLayers("World Terrain Reference")[0]
pop_map.removeLayer(labels)

boundary = pop_map.listLayers("oregon_bnd")[0]
sym = boundary.symbology
if boundary.isFeatureLayer and hasattr(sym, "renderer"):
    sym.updateRenderer('SimpleRenderer')
    symbol = sym.renderer.symbol
    symbol.applySymbolFromGallery("Black Outline (1pt)")
    sym.renderer.symbol = symbol
    boundary.symbology = sym

counties = pop_map.listLayers("counties")[0]
sym = counties.symbology
if counties.isFeatureLayer and hasattr(sym, "renderer"):
    sym.updateRenderer("GraduatedColorsRenderer")
    sym.renderer.classificationField = "POP_SQMI"
    sym.renderer.classificationMethod = "NaturalBreaks"
    sym.renderer.breakCount = 5
    sym.renderer.colorRamp = prj.listColorRamps("Oranges (5 Classes)")[0]
    counties.symbology = sym

# Set 50% transparency
counties.transparency = 50

# Label county names
label_classes = counties.listLabelClasses()
if label_classes:
    label_class = label_classes[0]
    label_class.expression = "$feature.NAME"
    label_class.visible = True
    counties.showLabels = True

prj.saveACopy("Exercise07_q4.aprx")
del prj

