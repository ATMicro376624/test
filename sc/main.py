from nbtschematic import SchematicFile
sf = SchematicFile.load("Test.schem")

print(sf['Schematic']["BlockData"])
print(sf['Schematic']["Palette"])

# Function to write blocks to a text file based on height layers
def write_blocks_to_file(sf, output_file):
    width = sf['Schematic']['Width']
    height = sf['Schematic']['Height']
    length = sf['Schematic']['Length']
    block_data = sf['Schematic']['BlockData']


    with open(output_file, 'w') as file:
        for z in range(height):
            file.write(f"Layer {z + 1} (Z={z + 1}):\n")
            for y in range(length):
                
                # Calculate the correct index range for each row
                row_start = (z * length + y) * width
                row_end = row_start + width

                #print(row_start,row_end)

                row_blocks = block_data[row_start:row_end]
                row_str = ' '.join(str(block) for block in row_blocks)

                #print(row_str)
                file.write(row_str + '\n')

# Specify the output file name
output_file_name = 'blocks_output.txt'

# Call the function to generate the text file
write_blocks_to_file(sf, output_file_name)

# Output file created
print(f'The blocks have been written to {output_file_name}.')