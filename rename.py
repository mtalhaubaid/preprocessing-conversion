import os

def rename_files_in_folder(folder_path):
    files = sorted(os.listdir(folder_path))  # Sort to maintain order
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):  # Ignore directories
            ext = os.path.splitext(filename)[1]  # Get file extension
            new_name = f"{i:05d}{ext}"  # Format as 00001, 00002, etc.
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

# Usage
folder_path = r"D:\user dataset\Aemen\lables"
rename_files_in_folder(folder_path)
