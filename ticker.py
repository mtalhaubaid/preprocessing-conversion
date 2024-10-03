from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os
from datetime import datetime
import re

def correct_bracket_pairs(reshaped_text):
    reshaped_text = re.sub(r'\((.*?)\)', r')\1(', reshaped_text)
    return reshaped_text

def generate_ocr_ticker(result, color, font_path):
    reshaped_text = arabic_reshaper.reshape(result)
    corrected_reshaped_text = correct_bracket_pairs(reshaped_text)
    bidi_text = get_display(corrected_reshaped_text)
    
    temp_tickers_ocr_dir = 'OCR'
    if not os.path.exists(temp_tickers_ocr_dir):
        os.makedirs(temp_tickers_ocr_dir)
    
    img_width, img_height = 800, 50
    if isinstance(color, str):
        color = tuple(map(int, color.split(',')))
    
    image = Image.new('RGB', (img_width, img_height), color=color)
    draw = ImageDraw.Draw(image)
    
    font_size = 36  # Increased font size
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Error: Font file '{font_path}' not found or cannot be opened.")
        return None
    
    print(f"Rendering text: {bidi_text}")
    
    # Calculate the size and position using textbbox
    text_bbox = draw.textbbox((0, 0), bidi_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2
    
    # Draw the text
    draw.text((text_x, text_y), bidi_text, font=font, fill=(0, 0, 0))  # Changed text color to black
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"ocr_ticker_{timestamp}.jpg"
    output_path = os.path.join(temp_tickers_ocr_dir, filename)
    image.save(output_path, 'JPEG', quality=95)
    return output_path

result_text = "وہ لیفٹیننٹ ہیں اور سے جنگیں لڑ چکے ہیں۔"
color = "255,165,0"
font_path = r"C:\Users\ASDF\Downloads\Jameel Noori Nastaleeq Regular\Jameel Noori Nastaleeq Regular.ttf"

output_image_path = generate_ocr_ticker(result_text, color, font_path)
if output_image_path:
    print(f"OCR ticker image saved at: {output_image_path}")
else:
    print("Failed to generate OCR ticker image.")
