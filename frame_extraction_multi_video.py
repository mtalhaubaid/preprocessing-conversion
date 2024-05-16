import cv2
import os

def extract_frames(video_path, output_folder, fps=2):
    """Extracts frames from a video and saves them in the specified output folder."""
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate / fps)

    frame_count = 0
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break  # Break loop if no frame is read

        if frame_count % frame_interval == 0:
            frame_output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_output_path, frame)
        frame_count += 1

    video_capture.release()
    print(f"Frames extracted: {frame_count}")
    print(f"Frames saved at {fps} fps in: {output_folder}")

if __name__ == "__main__":
    # Specify input video folder path
    input_video_folder = r"D:\user dataset\ANPR _New_dataset"  # Update with your folder path

    # Specify output root folder to save frames
    output_root_folder = r"multi_video_frame"  # Update with your folder path

    # Specify frame rate for frame extraction (frames per second)
    extraction_fps = 1

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]  # Add more extensions if needed

    # Process each video file
    for video_file in video_files:
        input_video_path = os.path.join(input_video_folder, video_file)
        # Create a folder with the same name as the video file to save frames
        video_name = os.path.splitext(video_file)[0] 
        output_folder = os.path.join(output_root_folder, video_name)  

        extract_frames(input_video_path, output_folder, fps=extraction_fps)
