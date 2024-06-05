
# Renames all files in a folder with sequential serial numbers (padded with zeros).

# Inputs: Path to the folder containing files to rename.
# Iterates through all files in the folder.
# Extracts the original file extension (e.g., .txt, .jpg).
# Constructs a new filename with a 3-digit serial number (padded with zeros) followed by the extension.
# Creates full paths for the original and new filenames.
# Attempts to rename the file using os.rename.
# Increments the counter for the next file.
# Handles potential errors if a file with the new name already exists.

import os

def rename_files_with_serial_numbers(folder_path):
    """Renames files in a folder with auto-incrementing serial numbers."""

    counter = 1

    for filename in os.listdir(folder_path):
        # Get the original file extension
        _, extension = os.path.splitext(filename)

        # Construct the new filename
        new_filename = f"{counter:03d}{extension}"  # e.g., 001.txt, 002.jpg

        # Get the full paths for the original and new filenames
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_path, new_path)  # Rename the file
            counter += 1
        except FileExistsError:
            print(f"Error: File '{new_filename}' already exists. Skipping...")


if __name__ == "__main__":
    folder_path = r"D:\code\annotations-conversion\multi_video_frame\all"

    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
    else:
        rename_files_with_serial_numbers(folder_path)
        print("Files renamed successfully!")
