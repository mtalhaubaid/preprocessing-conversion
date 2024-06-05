# Organizes images and annotations into separate folders within a given directory.

# Inputs: Path to a folder containing mixed image and annotation files.
# Creates "images" and "annotations" subfolders if they don't exist.
# Iterates through all files in the source folder.
# Moves images (JPG or PNG) to the "images" folder.
# Moves annotations (TXT) to the "annotations" folder.
# Uses os.replace to efficiently move files.



import os

def separate_images_annotations(source_folder):
  """
  Moves images and annotations to separate folders within the source folder.

  Args:
    source_folder: Path to the folder containing images and annotations.
  """
  image_folder = os.path.join(source_folder, "images")
  annotation_folder = os.path.join(source_folder, "labels")

  # Create folders if they don't exist
  os.makedirs(image_folder, exist_ok=True)
  os.makedirs(annotation_folder, exist_ok=True)

  for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg")or filename.endswith(".PNG") or filename.endswith(".JPG"):
      # Move image file
      source_path = os.path.join(source_folder, filename)
      destination_path = os.path.join(image_folder, filename)
      os.replace(source_path, destination_path)
    elif filename.endswith(".txt"):
      # Move annotation file
      source_path = os.path.join(source_folder, filename)
      destination_path = os.path.join(annotation_folder, filename)
      os.replace(source_path, destination_path)

# Replace 'path/to/your/folder' with your actual folder path
separate_images_annotations(r'D:\dataset\New folder\obj_train_data')
