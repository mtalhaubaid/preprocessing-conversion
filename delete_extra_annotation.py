import os

# Specify the directory containing the images and annotation files
directory = r'D:\code\yolov8-custom-training\numberplate_ocr\combine'

# List of valid image extensions
image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

# Collect all image file names (without extension)
image_files = {os.path.splitext(f)[0] for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in image_extensions}

# Iterate through all annotation files
for file_name in os.listdir(directory):
    if file_name.endswith('.txt'):
        # Check if there is a corresponding image file
        annotation_name = os.path.splitext(file_name)[0]
        if annotation_name not in image_files:
            # Delete the annotation file if no corresponding image file is found
            os.remove(os.path.join(directory, file_name))
            print(f"Deleted: {file_name}")
