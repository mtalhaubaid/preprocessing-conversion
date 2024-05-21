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
