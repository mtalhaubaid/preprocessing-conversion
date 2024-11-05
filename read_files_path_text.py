import os

# Define the directory containing .png files
directory = r"C:\Users\ASDF\Desktop\Alpha_Numeric\obj_train_data"

# Define the output text file path
output_file = r"C:\Users\ASDF\Desktop\Alpha_Numeric\train.txt"

# The relative path to append
relative_path = "Alpha_Numeric/obj_train_data"

# Open the text file in write mode
with open(output_file, 'w') as file:
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file ends with '.png'
        if filename.endswith('.png'):
            # Write the relative path along with the file name
            file.write(f"{relative_path}/{filename}\n")

print(f"PNG filenames with relative paths have been written to {output_file}")
