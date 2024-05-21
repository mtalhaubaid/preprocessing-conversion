import os

def separate_images_annotations(source_folder):
  """
  Moves images and annotations to separate folders within the source folder.

  Args:
    source_folder: Path to the folder containing images and annotations.
  """
  image_folder = os.path.join(source_folder, "images")
  annotation_folder = os.path.join(source_folder, "annotations")

  # Create folders if they don't exist
  os.makedirs(image_folder, exist_ok=True)
  os.makedirs(annotation_folder, exist_ok=True)

  for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
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
separate_images_annotations(r'D:\user dataset\car annotation t27c\removed empty anno')
