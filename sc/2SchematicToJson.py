from nbtschematic import SchematicFile
import json

#Load Json schematic File
sf = SchematicFile.load('RO1.schem')

#The write file name
file_path = "RO1.json"

sf_schematic = sf['Schematic']
# print(sf['Schematic']["Palette"])

# Json Data
data = {

    'Width': sf_schematic["Width"],
    'Height': sf_schematic["Height"],
    'Length': sf_schematic["Length"],
    'Palette' : sf_schematic["Palette"],
    'BlockData': list(sf_schematic['BlockData']),
    
}


# Writing data to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file)

print(f"JSON file has been created at: {file_path}")
