# Cleans up datasets by removing empty annotations and their associated images.
# Maintains data consistency by removing orphaned image files without annotations.
# Prints informative messages about deleted files.


import os

def process_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Separate .txt and .jpg files
    txt_files = [f for f in files if f.endswith('.txt')]
    jpg_files = [f for f in files if f.endswith('.jpg')]

    for txt_file in txt_files:
        txt_file_path = os.path.join(folder_path, txt_file)
        
        # Check if the .txt file is empty
        if os.path.getsize(txt_file_path) == 0:
            # Construct the corresponding .jpg file path
            jpg_file_path = os.path.join(folder_path, txt_file.replace('.txt', '.jpg'))
            
            # Delete the empty .txt file
            os.remove(txt_file_path)
            print(f"Deleted empty file: {txt_file_path}")
            
            # Delete the corresponding .jpg file if it exists
            if os.path.exists(jpg_file_path):
                os.remove(jpg_file_path)
                print(f"Deleted corresponding image: {jpg_file_path}")
            else:
                print(f"No corresponding image found for: {txt_file_path}")

if __name__ == "__main__":
    folder_path = r"C:\Users\ASDF\Downloads\suzuki data only\test\combine"  # Replace with the path to your folder
    process_files(folder_path)
