from PIL import Image 
from PIL import Image 
import PIL.Image
import numpy as np
import tifffile  # Make sure you have this installed: pip install tifffile

PIL.Image.MAX_IMAGE_PIXELS = None  # Remove decompression bomb limit 

def convert_tiff_to_png(tiff_path, output_path):
    img_array = tifffile.imread(tiff_path)  # Read with tifffile

    # Handle 16-bit grayscale (assuming single channel)
    if len(img_array.shape) == 2:
        scaled_array = (img_array / 255).astype(np.uint8)  # Normalize to 0-255
        # scaled_array = np.interp(img_array, [0, 65535], [0, 255]).astype(np.uint8)

        img = Image.fromarray(scaled_array)
    else:
        # Handle other cases (e.g., multi-channel images) as needed
        print("Image may have multiple channels or other format. Further handling might be needed.")

    img.save(output_path, "PNG")

# Specify your file paths
tiff_path = r"C:\Users\ASDF\Desktop\test.TIF"  
output_path = r"improved_converted.png"

# Call the conversion function
convert_tiff_to_png(tiff_path, output_path) 
print("Conversion successful.") 
