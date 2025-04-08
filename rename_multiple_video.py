import os
import time

# Folder path
folder_path = r"E:\dukto\cctv\frame blur weapons\gun shot 2"

# Supported video extensions
video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv')

# Get current timestamp
timestamp = time.strftime('%Y%m%d_%H%M%S')

# Counter
counter = 1

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(video_extensions):
        old_path = os.path.join(folder_path, filename)
        file_ext = os.path.splitext(filename)[1]
        new_filename = f"{timestamp}_{counter}{file_ext}"
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_filename}")
        counter += 1

print("\n✅ All video files renamed successfully.")
