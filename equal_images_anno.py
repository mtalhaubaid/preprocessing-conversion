import os

def delete_unannotated_images(directory):
    # Supported image file extensions
    image_extensions = {".jpg", ".JPG", ".JPEG", ".jpeg", ".PNG", ".png"}
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Create a set of annotation file base names (without extension)
    annotation_basenames = {os.path.splitext(f)[0] for f in files if f.endswith('.txt')}
    
    # Iterate through all files in the directory
    for file in files:
        # Get file extension
        file_ext = os.path.splitext(file)[1]
        
        # Check if the file is an image
        if file_ext in image_extensions:
            # Get the base name of the image file (without extension)
            base_name = os.path.splitext(file)[0]
            
            # Check if the corresponding annotation file exists
            if base_name not in annotation_basenames:
                # Construct the full path to the image file
                file_path = os.path.join(directory, file)
                
                # Delete the image file
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Example usage
directory_path = r"C:\Users\ASDF\Desktop\Alpha & Numeric\obj_train_data"  # Replace with the path to your directory
delete_unannotated_images(directory_path)
