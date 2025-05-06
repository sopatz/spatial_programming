# Lab 7 Question 3
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/PythonPro/Exercise07'

prj = arcpy.mp.ArcGISProject("Exercise07.aprx")
oregon_map = prj.listMaps("Oregon")[0]
oregon_map.addBasemap("Topographic")

boundary = oregon_map.listLayers("oregon_bnd")[0]
sym = boundary.symbology

if boundary.isFeatureLayer and hasattr(sym, "renderer"):
    sym.updateRenderer('SimpleRenderer')
    symbol = sym.renderer.symbol
    symbol.applySymbolFromGallery("Dashed Black Outline (1pt)")
    # Apply changes
    sym.renderer.symbol = symbol
    boundary.symbology = sym

oregon_map.addDataFromPath('C:/PythonPro/Exercise07/Exercise07.gdb/majcities')
oregon_map.addDataFromPath('C:/PythonPro/Exercise07/Exercise07.gdb/highways')

# Apply symbology to majcities
majcities_layer = oregon_map.listLayers("majcities")[0]
sym = majcities_layer.symbology

if majcities_layer.isFeatureLayer and hasattr(sym, "renderer"):
    sym.updateRenderer("SimpleRenderer")
    symbol = sym.renderer.symbol
    symbol.applySymbolFromGallery("Circle 3", 1)
    symbol.color = {'RGB': [230, 0, 0, 100]}  # Poinsettia red
    sym.renderer.symbol = symbol
    majcities_layer.symbology = sym

rivers = oregon_map.listLayers("rivers")[0]
oregon_map.removeLayer(rivers)

volcanoes_layer = oregon_map.listLayers("volcanoes")[0]
sym = volcanoes_layer.symbology

if volcanoes_layer.isFeatureLayer and hasattr(sym, "renderer"):
    sym.updateRenderer("SimpleRenderer")
    symbol = sym.renderer.symbol
    symbol.applySymbolFromGallery("Triangle 3")
    
    #Color as the instructions specify
    #(Don't know why we're putting in color but making it transparent too)
    symbol.color = {'RGB': [56, 168, 0, 0]}
    sym.renderer.symbol = symbol
    volcanoes_layer.symbology = sym

prj.saveACopy("Exercise07_q3.aprx")
del prj

