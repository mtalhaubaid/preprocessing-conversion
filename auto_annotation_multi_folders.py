import os
from ultralytics.data.annotator import auto_annotate

def process_subfolders(root_folder, det_model_path):
    """
    Iterates over subfolders within the root folder, 
    passing each subfolder path to the auto_annotate function.
    """
    for subfolder_name in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder_name)

        # Check if the path is a directory before processing
        if os.path.isdir(subfolder_path): 
            print(f"Processing subfolder: {subfolder_name}")
            auto_annotate(data=subfolder_path, det_model=det_model_path)

if __name__ == "__main__":
    root_folder = r'D:\code\annotations-conversion\multi_video_frame'
    det_model_path = 'yolov8x.pt'  # Make sure the model is in the right location
    process_subfolders(root_folder, det_model_path)


    
