import os
import shutil

def collect_images(source_dir, target_dir, extensions=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")):
    os.makedirs(target_dir, exist_ok=True)  # Create target folder if it doesn't exist
    
    count = 1
    for root, _, files in os.walk(source_dir):  # Recursively walk through directories
        for file in files:
            if file.lower().endswith(extensions):  # Check if it's an image
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, f"{count:05d}{os.path.splitext(file)[1]}")  # Rename sequentially
                shutil.copy2(source_path, target_path)  # Copy file
                print(f"Copied: {source_path} → {target_path}")
                count += 1

# Paths
source_directory = r"C:\Users\ASDF\Desktop\Aemen\folders to merge"
target_directory = r"C:\Users\ASDF\Desktop\Aemen\merged_images"

collect_images(source_directory, target_directory)
