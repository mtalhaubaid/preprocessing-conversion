import os
import cv2
import albumentations as A
import numpy as np
import shutil

# Define paths
images_path = 'path_to_your_images_folder'
annotations_path = 'path_to_your_annotations_folder'
output_images_path = 'path_to_output_augmented_images'
output_annotations_path = 'path_to_output_augmented_annotations'

# Create output directories if not exist
os.makedirs(output_images_path, exist_ok=True)
os.makedirs(output_annotations_path, exist_ok=True)

# Define augmentation pipeline
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=15, p=0.5),
    A.Blur(blur_limit=3, p=0.2),
    A.GaussianNoise(p=0.2),
    A.ColorJitter(p=0.2),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=45, p=0.5)
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

def read_yolo_annotation(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    bboxes = []
    class_labels = []
    for line in lines:
        data = line.strip().split()
        class_labels.append(int(data[0]))
        bboxes.append([float(x) for x in data[1:]])
    return bboxes, class_labels

def write_yolo_annotation(file_path, bboxes, class_labels):
    with open(file_path, 'w') as file:
        for bbox, label in zip(bboxes, class_labels):
            file.write(f"{label} " + " ".join(map(str, bbox)) + "\n")

# Process each image and corresponding annotation
for image_file in os.listdir(images_path):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        image_path = os.path.join(images_path, image_file)
        annotation_file = os.path.splitext(image_file)[0] + '.txt'
        annotation_path = os.path.join(annotations_path, annotation_file)

        # Read image and annotation
        image = cv2.imread(image_path)
        bboxes, class_labels = read_yolo_annotation(annotation_path)

        # Apply augmentation
        augmented = transform(image=image, bboxes=bboxes, class_labels=class_labels)
        aug_image = augmented['image']
        aug_bboxes = augmented['bboxes']
        aug_class_labels = augmented['class_labels']

        # Save augmented image and corresponding annotation
        output_image_path = os.path.join(output_images_path, 'aug_' + image_file)
        output_annotation_path = os.path.join(output_annotations_path, 'aug_' + annotation_file)
        cv2.imwrite(output_image_path, aug_image)
        write_yolo_annotation(output_annotation_path, aug_bboxes, aug_class_labels)
        
        print(f"Augmented and saved: {image_file}")

print("Data augmentation completed.")
