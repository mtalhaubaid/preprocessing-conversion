from PIL import Image
import os

# Define the folder path and target dimensions
folder_path = r'C:\Users\ASDF\Desktop\temp\images'
target_size = (69, 50)

# Create a function to resize images
def resize_images_in_folder(folder_path, target_size):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)

        # Open an image file
        with Image.open(file_path) as img:
            # Resize the image
            resized_img = img.resize(target_size)

            # Save the resized image back to the same path
            resized_img.save(file_path)

# Call the function
resize_images_in_folder(folder_path, target_size)

print("All images have been resized to 69x50 pixels.")
