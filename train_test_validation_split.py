# This Python code splits a dataset images and annotations (text files) into training, validation, and test sets. 
# It shuffles the data for randomness and ensures each image has a corresponding annotation. 
# The script creates folders for the split data and copies the corresponding image-annotation pairs into their respective folders.


import os
import shutil
import random

# Define the paths
images_path = r"D:\apha_numeric_746\augmented_dataset\all\images"
annotations_path = r"D:\apha_numeric_746\augmented_dataset\all\anno"
output_path = r"D:\apha_numeric_746\augmented_dataset\all_splitted_data"

# Define the output directories
train_images_path = os.path.join(output_path, 'train', 'images')
train_annotations_path = os.path.join(output_path, 'train', 'labels')
valid_images_path = os.path.join(output_path, 'valid', 'images')
valid_annotations_path = os.path.join(output_path, 'valid', 'labels')
test_images_path = os.path.join(output_path, 'test', 'images')
test_annotations_path = os.path.join(output_path, 'test', 'labels')

# Create the output directories
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_annotations_path, exist_ok=True)
os.makedirs(valid_images_path, exist_ok=True)
os.makedirs(valid_annotations_path, exist_ok=True)
os.makedirs(test_images_path, exist_ok=True)
os.makedirs(test_annotations_path, exist_ok=True)

# Get list of all image files and annotations
images = os.listdir(images_path)
annotations = os.listdir(annotations_path)

# Ensure the images and annotations lists are sorted
images.sort()
annotations.sort()

# Check that every image has a corresponding annotation
image_files = [f for f in images if os.path.isfile(os.path.join(images_path, f))]
annotation_files = [f for f in annotations if os.path.isfile(os.path.join(annotations_path, f))]

# Shuffle the dataset
random.seed(42)
combined = list(zip(image_files, annotation_files))
random.shuffle(combined)
image_files, annotation_files = zip(*combined)

# Calculate split sizes
total_files = len(image_files)
train_size = int(total_files * 0.7)
valid_size = int(total_files * 0.2)

# Split the dataset
train_images = image_files[:train_size]
train_annotations = annotation_files[:train_size]
valid_images = image_files[train_size:train_size + valid_size]
valid_annotations = annotation_files[train_size:train_size + valid_size]
test_images = image_files[train_size + valid_size:]
test_annotations = annotation_files[train_size + valid_size:]

# Function to copy files to the designated folder
def copy_files(file_list, source_folder, dest_folder):
    for file in file_list:
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_folder, file))

# Copy the files to their respective directories
copy_files(train_images, images_path, train_images_path)
copy_files(train_annotations, annotations_path, train_annotations_path)
copy_files(valid_images, images_path, valid_images_path)
copy_files(valid_annotations, annotations_path, valid_annotations_path)
copy_files(test_images, images_path, test_images_path)
copy_files(test_annotations, annotations_path, test_annotations_path)

print(f"Train set: {len(train_images)} images and annotations")
print(f"Validation set: {len(valid_images)} images and annotations")
print(f"Test set: {len(test_images)} images and annotations")