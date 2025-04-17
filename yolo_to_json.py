import os
import json
from PIL import Image

# Update paths
images_dir = r'E:\dukto\animals\images'
labels_dir = r'E:\dukto\animals\label'
output_file = 'label_studio_yolo_import.json'

annotations = []

for filename in os.listdir(labels_dir):
    if filename.endswith('.txt'):
        image_filename = filename.replace('.txt', '.jpg')  # or .png
        image_path = os.path.join(images_dir, image_filename)
        
        # Skip if image not found
        if not os.path.exists(image_path):
            continue

        width, height = Image.open(image_path).size

        with open(os.path.join(labels_dir, filename), 'r') as f:
            boxes = []
            for line in f.readlines():
                cls, x_center, y_center, w, h = map(float, line.strip().split())
                x = (x_center - w/2) * width
                y = (y_center - h/2) * height
                w *= width
                h *= height

                boxes.append({
                    "label": ["class_{}".format(int(cls))],
                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h,
                    "type": "rectangle",
                })

        annotations.append({
            "data": {"image": image_path},
            "annotations": [{"result": [{"value": b, "from_name": "label", "to_name": "image", "type": "rectanglelabels"} for b in boxes]}]
        })

with open(output_file, 'w') as f:
    json.dump(annotations, f, indent=2)
