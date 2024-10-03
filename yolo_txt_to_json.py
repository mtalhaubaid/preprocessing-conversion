import json
import os
from PIL import Image

# Set paths for images and annotations
images_dir = r'C:\Users\ASDF\Desktop\Yolov5_ocr_charater_working\images'
annotations_dir = r'C:\Users\ASDF\Desktop\Yolov5_ocr_charater_working\annotations'
output_dir = r'C:\Users\ASDF\Desktop\Yolov5_ocr_charater_working\output_json'

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each annotation file
for filename in os.listdir(annotations_dir):
    if filename.endswith('.txt'):
        # Extract base name and set image path
        base_filename = os.path.splitext(filename)[0]
        image_path = os.path.join(images_dir, base_filename + '.png')
        json_path = os.path.join(output_dir, base_filename + '.json')

        # Open image to get dimensions
        with Image.open(image_path) as img:
            width, height = img.size

        # Initialize JSON structure
        data = {
            'version': '1.0',
            'type': 'annotations',
            'labels': [],
            'image': {
                'width': width,
                'height': height
            },
            'shapes': []
        }

        # Read annotations from file
        with open(os.path.join(annotations_dir, filename), 'r') as file:
            for line in file:
                parts = line.strip().split()
                label_id, x_center, y_center, bbox_width, bbox_height = map(float, parts)
                xmin = (x_center - bbox_width / 2) * width
                xmax = (x_center + bbox_width / 2) * width
                ymin = (y_center - bbox_height / 2) * height
                ymax = (y_center + bbox_height / 2) * height

                # Append annotation to the list
                data['shapes'].append({
                    'type': 'rectangle',
                    'label': str(int(label_id)),
                    'points': [[xmin, ymin], [xmax, ymax]]
                })

        # Write data to JSON file
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)

print("Conversion complete. JSON files are saved in:", output_dir)
