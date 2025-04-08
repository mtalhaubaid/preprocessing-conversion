import os
from pathlib import Path

def sync_images_and_annotations(images_dir, labels_dir, image_exts=(".jpg", ".jpeg", ".png"), annotation_ext=".txt"):
    images_dir = Path(images_dir)
    labels_dir = Path(labels_dir)

    # Collect all image and annotation stem names (filenames without extension)
    image_files = {f.stem for f in images_dir.glob("*") if f.suffix.lower() in image_exts}
    label_files = {f.stem for f in labels_dir.glob("*") if f.suffix.lower() == annotation_ext}

    # Images without annotations
    orphan_images = image_files - label_files
    # Annotations without images
    orphan_labels = label_files - image_files

    # Delete orphan images
    for img_stem in orphan_images:
        for ext in image_exts:
            img_path = images_dir / f"{img_stem}{ext}"
            if img_path.exists():
                os.remove(img_path)
                print(f"Deleted image: {img_path}")

    # Delete orphan labels
    for label_stem in orphan_labels:
        label_path = labels_dir / f"{label_stem}{annotation_ext}"
        if label_path.exists():
            os.remove(label_path)
            print(f"Deleted annotation: {label_path}")

    print("\n✅ Synchronization complete.")

# Example usage
sync_images_and_annotations(
    images_dir=r"D:\dataset\weapons\yolo_training\images",
    labels_dir=r"D:\dataset\weapons\yolo_training\labels"
)
