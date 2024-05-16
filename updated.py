import os
import shutil
import random
from sklearn.model_selection import train_test_split

def split_dataset(image_dir, annotation_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=None):
    """Splits a dataset of images and annotations into train, test, and validation sets.

    Args:
        image_dir (str): Path to the directory containing images.
        annotation_dir (str): Path to the directory containing annotations.
        train_ratio (float): Ratio for the training set (default: 0.7).
        val_ratio (float): Ratio for the validation set (default: 0.15).
        test_ratio (float): Ratio for the test set (default: 0.15).
        seed (int): Random seed for reproducibility (default: None).
    """

    if not os.path.exists(image_dir):
        raise ValueError(f"Image directory not found: {image_dir}")
    if not os.path.exists(annotation_dir):
        raise ValueError(f"Annotation directory not found: {annotation_dir}")

    if train_ratio + val_ratio + test_ratio != 1:
        raise ValueError("Train, validation, and test ratios must sum to 1")

    image_filenames = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    annotation_filenames = [f for f in os.listdir(annotation_dir) if os.path.isfile(os.path.join(annotation_dir, f))]

    # Handle mismatches
    common_filenames = set(image_filenames) & set(annotation_filenames)

    random.seed(seed)
    train_val, test = train_test_split(list(common_filenames), test_size=test_ratio) # Convert to list
    train, val = train_test_split(train_val, test_size=val_ratio / (train_ratio + val_ratio))

    splits = {'train': train, 'val': val, 'test': test}
    for split in splits:
        os.makedirs(os.path.join(image_dir, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(image_dir, split, 'labels'), exist_ok=True)
        os.makedirs(os.path.join(annotation_dir, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(annotation_dir, split, 'labels'), exist_ok=True)

        for filename in splits[split]:
            shutil.move(os.path.join(image_dir, filename), os.path.join(image_dir, split, 'images', filename))
            shutil.move(os.path.join(annotation_dir, filename), os.path.join(annotation_dir, split, 'labels', filename))

if __name__ == "__main__":
    image_dir = r"D:\dataset\weapon\all\all data\images"  # Replace with your image folder path
    annotation_dir = r"D:\dataset\weapon\all\all data\labels"  # Replace with your annotation folder path
    split_dataset(image_dir, annotation_dir)
