# from PIL import Image, ImageDraw, ImageFont
# import arabic_reshaper
# from bidi.algorithm import get_display
# import os
# from datetime import datetime

# def generate_ocr_ticker(result, color, font_path):
#     # Reshape the Arabic text for correct rendering
#     reshaped_text = arabic_reshaper.reshape(result)
#     bidi_text = get_display(reshaped_text)

#     # Set up the output directory
#     output_dir = 'OCR'
#     os.makedirs(output_dir, exist_ok=True)

#     # Define image dimensions and create a new image with the specified background color
#     img_width, img_height = 800, 50
#     image = Image.new('RGB', (img_width, img_height), color=color)
#     draw = ImageDraw.Draw(image)

#     # Load the specified font
#     font_size = 36
#     try:
#         font = ImageFont.truetype(font_path, font_size)
#     except Exception as e:
#         print(f"Failed to load specified font due to: {e}. Using default font.")
#         font = ImageFont.load_default()

#     # Calculate text dimensions and position
#     text_width, text_height = draw.textbbox((0, 0), bidi_text, font=font)[2:4]
#     text_x = (img_width - text_width) / 2
#     text_y = (img_height - text_height) / 2

#     # Draw the text onto the image
#     draw.text((text_x, text_y), bidi_text, font=font, fill=(0, 0, 0))

#     # Save the image
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     filename = f"ocr_ticker_{timestamp}.jpg"
#     filepath = os.path.join(output_dir, filename)
#     image.save(filepath, 'JPEG', quality=95)
    
#     return filepath

# # Example usage
# result_text = "وہ لیفٹیننٹ ہیں اور سے جنگیں لڑ چکے ہیں۔"
# color = (255, 165, 0)  # Orange background using RGB tuple
# font_path = r"C:\Users\ASDF\Downloads\Jameel Noori Nastaleeq Regular\Jameel Noori Nastaleeq Regular.ttf"  # Ensure this path is correct

# output_image_path = generate_ocr_ticker(result_text, color, font_path)
# print(f"OCR ticker image saved at: {output_image_path}")




from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os
from datetime import datetime

def generate_ocr_ticker(result, color, font_path):
    # Reshape the Arabic text for correct rendering
    reshaped_text = arabic_reshaper.reshape(result)
    bidi_text = get_display(reshaped_text)

    # Set up the output directory
    output_dir = 'OCR'
    os.makedirs(output_dir, exist_ok=True)

    # Define image dimensions and create a new image with the specified background color
    img_width, img_height = 800, 50
    image = Image.new('RGB', (img_width, img_height), color=color)
    draw = ImageDraw.Draw(image)

    # Load the specified font with Raqm layout engine if available
    font_size = 36
    try:
        font = ImageFont.truetype(font_path, font_size, layout_engine=ImageFont.LAYOUT_RAQM)
    except IOError:
        print(f"Failed to load specified font due to: IOError. Using default font.")
        font = ImageFont.load_default()
    except AttributeError:
        # Fall back if Raqm is not available
        print("Raqm layout engine not available. Falling back to default layout engine.")
        font = ImageFont.truetype(font_path, font_size)

    # Calculate text dimensions and position
    text_width, text_height = draw.textbbox((0, 0), bidi_text, font=font)[2:4]
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2

    # Draw the text onto the image
    draw.text((text_x, text_y), bidi_text, font=font, fill=(0, 0, 0))

    # Save the image
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"ocr_ticker_{timestamp}.jpg"
    filepath = os.path.join(output_dir, filename)
    image.save(filepath, 'JPEG', quality=95)
    
    return filepath

# Example usage
result_text = "وہ لیفٹیننٹ ہیں اور سے جنگیں لڑ چکے ہیں۔"
color = (255, 165, 0)  # Orange background using RGB tuple
font_path = r"C:\Users\ASDF\Downloads\Jameel Noori Nastaleeq Regular\Jameel Noori Nastaleeq Regular.ttf"  # Ensure this path is correct

output_image_path = generate_ocr_ticker(result_text, color, font_path)
print(f"OCR ticker image saved at: {output_image_path}")
