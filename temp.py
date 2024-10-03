import os

# Define the image directory and the output file
image_dir = r'C:\Users\ASDF\Desktop\Yolov5_ocr_charater_working\images'
output_file = 'train.txt'
prefix_path = 'data/obj_train_data/'

# Get the list of all image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Open the output file in write mode
with open(output_file, 'w') as f:
    # Loop through all image files
    for image in image_files:
        # Write the desired path format to the file
        f.write(f"{prefix_path}{image}\n")

print(f"Train file '{output_file}' has been created with the image paths.")
