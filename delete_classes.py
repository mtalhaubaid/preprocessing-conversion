# Filters text files based on line content, keeping only lines starting with specific characters.

# Inputs: Path to the folder containing text files.
# Iterates through all files ending with ".txt" in the folder.
# Reads all lines from the current file.
# Prints the original lines for debugging purposes (optional).
# Iterates through each line:
# Removes leading/trailing whitespaces using strip().
# Prints the stripped line and its first character for debugging (optional).
# Filters lines where the stripped line is not empty and the first character is either '7', '2', or '5'.
# Prints lines being removed for debugging (optional).
# Creates a new list containing only the filtered lines.
# Prints the filtered lines for debugging (optional).
# Overwrites the original file content with the filtered lines.


import os

def process_files_in_folder(folder_path):
    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Debug: Print the original lines
            print(f"Processing file: {filename}")
            print("Original lines:")
            for line in lines:
                print(f"'{line.strip()}'")

            # Filter lines that start with "7", "2", or "5"
            filtered_lines = []
            for line in lines:
                stripped_line = line.strip()
                # Debug: Print the stripped line and the first character
                print(f"Stripped line: '{stripped_line}' | First char: '{stripped_line[0]}'" if stripped_line else "Empty line")
                if stripped_line and stripped_line[0] in {'7', '2', '5'}:
                    filtered_lines.append(line)
                else:
                    print(f"Removing line: '{line.strip()}'")

            # Debug: Print the filtered lines
            print("Filtered lines:")
            for line in filtered_lines:
                print(f"'{line.strip()}'")

            # Write the filtered lines back to the file
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)

# Specify the folder path
folder_path = r'D:\code\annotations-conversion\multi_video_frame\all_check'
process_files_in_folder(folder_path)





