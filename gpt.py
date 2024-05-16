import os
import random
import shutil

def split_dataset(images_dir, annotations_dir, output_dir, train_ratio=0.7, test_ratio=0.15, valid_ratio=0.15):
    # Create output directories
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    valid_dir = os.path.join(output_dir, 'valid')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)
    
    # Get list of image and annotation files
    image_files = os.listdir(images_dir)
    annotation_files = os.listdir(annotations_dir)
    
    # Shuffle the files
    random.shuffle(image_files)
    
    # Calculate split sizes
    total_samples = len(image_files)
    train_size = int(total_samples * train_ratio)
    test_size = int(total_samples * test_ratio)
    
    # Assign files to train, test, and valid sets
    train_images = image_files[:train_size]
    test_images = image_files[train_size:train_size + test_size]
    valid_images = image_files[train_size + test_size:]
    
    # Move image files to corresponding directories
    for img in train_images:
        shutil.copy(os.path.join(images_dir, img), os.path.join(train_dir, 'images'))
        shutil.copy(os.path.join(annotations_dir, img.replace('.jpg', '.txt')), os.path.join(train_dir, 'labels'))
    
    for img in test_images:
        shutil.copy(os.path.join(images_dir, img), os.path.join(test_dir, 'images'))
        shutil.copy(os.path.join(annotations_dir, img.replace('.jpg', '.txt')), os.path.join(test_dir, 'labels'))
    
    for img in valid_images:
        shutil.copy(os.path.join(images_dir, img), os.path.join(valid_dir, 'images'))
        shutil.copy(os.path.join(annotations_dir, img.replace('.jpg', '.txt')), os.path.join(valid_dir, 'labels'))

# Example usage
images_dir = r'D:\dataset\weapon\all\all data\images'  # Directory containing image files
annotations_dir = r'D:\dataset\weapon\all\all data\labels'  # Directory containing annotation files
output_dir = 'out'  # Directory where the split dataset will be saved
split_dataset(images_dir, annotations_dir, output_dir)
