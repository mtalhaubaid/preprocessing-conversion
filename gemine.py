import os
import shutil
import random

def split_dataset(image_dir, annotation_dir, output_dir, train_ratio=0.7, test_ratio=0.15, valid_ratio=0.15):
    """
    Splits a dataset of images and annotations into train, test, and validation sets.

    Args:
        image_dir (str): Path to the directory containing images.
        annotation_dir (str): Path to the directory containing annotations.
        output_dir (str): Path to the output directory where the split sets will be created.
        train_ratio (float, optional): Proportion of the dataset to allocate for the training set. Defaults to 0.7.
        test_ratio (float, optional): Proportion of the dataset to allocate for the test set. Defaults to 0.15.
        valid_ratio (float, optional): Proportion of the dataset to allocate for the validation set. Defaults to 0.15.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the list of image filenames
    image_filenames = [f for f in os.listdir(image_dir) if f.endswith('.JPG')]

    # Calculate the number of samples for each set
    num_samples = len(image_filenames)
    num_train = int(train_ratio * num_samples)
    num_test = int(test_ratio * num_samples)
    num_valid = num_samples - num_train - num_test 

    # Shuffle the image filenames for randomness
    random.shuffle(image_filenames)

    # Split the image filenames into train, test, and validation sets
    train_set = image_filenames[:num_train]
    test_set = image_filenames[num_train:num_train + num_test]
    valid_set = image_filenames[num_train + num_test:]

    # Create the output folders
    for split in ['train', 'test', 'valid']:
        os.makedirs(os.path.join(output_dir, split, 'images'))
        os.makedirs(os.path.join(output_dir, split, 'labels'))

    # Copy images and annotations to their respective folders
    for filename in train_set:
        image_path = os.path.join(image_dir, filename)
        annotation_path = os.path.join(annotation_dir, filename.replace('.JPG', '.txt'))
        shutil.copy(image_path, os.path.join(output_dir, 'train', 'images', filename))
        shutil.copy(annotation_path, os.path.join(output_dir, 'train', 'labels', filename.replace('.JPG', '.txt')))

    for filename in test_set:
        image_path = os.path.join(image_dir, filename)
        annotation_path = os.path.join(annotation_dir, filename.replace('.JPG', '.txt'))
        shutil.copy(image_path, os.path.join(output_dir, 'test', 'images', filename))
        shutil.copy(annotation_path, os.path.join(output_dir, 'test', 'labels', filename.replace('.JPG', '.txt')))

    for filename in valid_set:
        image_path = os.path.join(image_dir, filename)
        annotation_path = os.path.join(annotation_dir, filename.replace('.JPG', '.txt'))
        shutil.copy(image_path, os.path.join(output_dir, 'valid', 'images', filename))
        shutil.copy(annotation_path, os.path.join(output_dir, 'valid', 'labels', filename.replace('.JPG', '.txt')))

# Example usage - Replace with your actual directory paths
image_dir = r'D:\dataset\weapon\all\all data\images'
annotation_dir = r'D:\dataset\weapon\all\all data\labels'
output_dir = 'folder'

split_dataset(image_dir, annotation_dir, output_dir)