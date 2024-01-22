from nbtschematic import SchematicFile
import json

#Load Json schematic File
sf = SchematicFile.load('TESpawn.schem')

#The write file name
file_path = "example1.json"

sf_schematic = sf['Schematic']
# print(sf['Schematic']["Palette"])

# Json Data

BlockData = []
stringy = ""

for i in sf_schematic['BlockData']:

    integer = int(i)


    if 0 <= integer <= 9:
        stringy += str(int(i))
    else:

        if stringy != "":
            BlockData.append(stringy)
        
        BlockData.append(i)
        stringy = ""

    

 

data = {

    'Width': sf_schematic["Width"],
    'Height': sf_schematic["Height"],
    'Length': sf_schematic["Length"],
    'Palette' : sf_schematic["Palette"],
    'BlockData': BlockData,
}


# Writing data to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file)

print(f"JSON file has been created at: {file_path}")
