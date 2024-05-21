# import os

# def process_files_in_folder(folder_path):
#     # Iterate over all files in the given folder
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(folder_path, filename)
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
            
#             # Filter lines that start with "7", "2", or "5"
#             filtered_lines = [line for line in lines if line.startswith(('7', '2', '5'))]
            
#             # Write the filtered lines back to the file
#             with open(file_path, 'w') as file:
#                 file.writelines(filtered_lines)

# # Specify the folder path
# folder_path = r'D:\code\annotations-conversion\multi_video_frame\all_check'
# process_files_in_folder(folder_path)



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





