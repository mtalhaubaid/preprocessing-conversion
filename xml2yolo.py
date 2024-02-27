import xml.etree.ElementTree as ET
import os

def convert_xml_to_yolo(xml_path, output_dir, class_mapping):
    """Converts a single XML annotation file to YOLO format.

    Args:
        xml_path (str): The path to the XML annotation file.
        output_dir (str): The directory to save the YOLO formatted text file.
        class_mapping (dict): A dictionary mapping class names to YOLO class IDs.
    """

    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    objects = root.findall('object')
    with open(os.path.join(output_dir, os.path.splitext(os.path.basename(xml_path))[0] + '.txt'), 'w') as f:
        for obj in objects:
            class_name = obj.find('name').text
            if class_name not in class_mapping:
                print(f"Warning: Class '{class_name}' not found in class mapping. Skipping.")
                continue

            class_id = class_mapping[class_name]

            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            # Normalize coordinates (0-1)
            x_center = ((xmin + xmax) / 2) / width 
            y_center = ((ymin + ymax) / 2) / height
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height

            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

def main():
    xml_dir = r'D:\dataset\weapon\Test\Annotations'  # Replace with your XML directory
    output_dir = r'D:\dataset\weapon\Test\yolo annoatation'  # Replace with your desired output directory
    class_mapping = {
        'gun': 0,  # Replace 'class1' with your actual class name and assign the correct YOLO ID
    }

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_file)
            convert_xml_to_yolo(xml_path, output_dir, class_mapping)

if __name__ == '__main__':
    main()
