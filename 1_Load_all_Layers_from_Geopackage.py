
from osgeo import ogr

# Define the path to the .gkg 
geo_package_path = r"C:\Users\jjtakodjou\Desktop\SpatialThoughts\Data\karnataka.gpkg"
# geo_package_path = "C:/Users/jjtakodjou/Desktop/SpatialThoughts/Data/karnataka.gpkg"

# Get layer name inside the geopackage
layers_names = [layer.GetName() for layer in ogr.Open(geo_package_path)]
print(layers_names)

# Loop over the layer_names
for layer in layers_names:
    # append the name of the layer to the path of the geopackage 
    gpkg_countries_layer = geo_package_path + f"|layername={layer}"
    # Create a vector layer
    vlayer = QgsVectorLayer(gpkg_countries_layer, layer, "ogr")
    if not vlayer.isValid():
        print("Layer failed to load!")
    else:
        # Add the layer to the current project
        QgsProject.instance().addMapLayer(vlayer)
   