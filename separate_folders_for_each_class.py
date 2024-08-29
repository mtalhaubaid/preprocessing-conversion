import os
import shutil

# Define the paths
yolo_folder = r'D:\user dataset\car_brand_detection_public_dataset\complete data_set'
class_folder = r'D:\user dataset\car_brand_detection_public_dataset\separate folders'

# Define the classes
classes = ["Audi", "BMW", "Honda", "Hyundai", "Kia", "Lexus", "Mercedes", "Mitsubishi", "Nissan", "Suzuki", "Toyota"]

# Create class subfolders if they do not exist
for class_name in classes:
    class_path = os.path.join(class_folder, class_name)
    if not os.path.exists(class_path):
        os.makedirs(class_path)

# Function to get class name from YOLO annotation
def get_class_name(annotation_path):
    with open(annotation_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line:
            class_index = int(first_line.split()[0])
            if class_index < len(classes):
                return classes[class_index]
    return None

# Process each annotation and corresponding image
for file_name in os.listdir(yolo_folder):
    if file_name.endswith('.txt'):
        annotation_path = os.path.join(yolo_folder, file_name)
        image_path = annotation_path.replace('.txt', '.jpg')  # Assuming image extension is .jpg

        class_name = get_class_name(annotation_path)
        if class_name:
            class_path = os.path.join(class_folder, class_name)

            # Move annotation and image to the respective class folder
            shutil.move(annotation_path, os.path.join(class_path, file_name))
            if os.path.exists(image_path):
                shutil.move(image_path, os.path.join(class_path, os.path.basename(image_path)))

print("Files have been successfully separated into their respective class folders.")
