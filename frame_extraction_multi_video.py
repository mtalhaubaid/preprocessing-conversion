# Extracts frames from videos at a specified frame rate and saves them in separate folders.

# Inputs: Path to the folder containing videos, path to the output folder root, desired frames per second (fps).
# Iterates through all video files (MP4, AVI, MKV by default) in the input folder.
# Creates an output folder with the same name as the video file to store extracted frames.
# Opens the video using OpenCV.
# Calculates total frames, frame rate, and frame interval based on desired fps.
# Reads frames in a loop, breaking when no frame is available.
# Saves frames only at specified intervals based on the frame rate.
# Uses cv2.imwrite to write each frame as a JPEG image.
# Prints information about extracted frames and their location.

import cv2
import os

def extract_frames(video_path, output_folder, fps=2):
    """Extracts frames from a video and saves them in the specified output folder."""
    os.makedirs(output_folder, exist_ok=True)

    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)

    if frame_rate == 0 or fps == 0:
        print(f"⚠️ Skipping {video_path}: frame_rate={frame_rate}, fps={fps}")
        return

    frame_interval = int(frame_rate / fps)
    if frame_interval == 0:
        frame_interval = 1  # Ensure we don't skip all frames if fps is very high

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_output_path, frame)
            saved_count += 1

        frame_count += 1

    video_capture.release()
    print(f"Frames extracted: {saved_count}")
    print(f"Frames saved at {fps} fps in: {output_folder}")


if __name__ == "__main__":
    # Specify input video folder path
    input_video_folder = r"E:\dukto\cctv\frame blur weapons\gun shot 2"  # Update with your folder path

    # Specify output root folder to save frames
    output_root_folder = r"E:\dukto\cctv\frame blur weapons\frames"  # Update with your folder path

    # Specify frame rate for frame extraction (frames per second)
    extraction_fps = 60

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]  # Add more extensions if needed

    # Process each video file
    for video_file in video_files:
        input_video_path = os.path.join(input_video_folder, video_file)
        # Create a folder with the same name as the video file to save frames
        video_name = os.path.splitext(video_file)[0] 
        output_folder = os.path.join(output_root_folder, video_name)  

        extract_frames(input_video_path, output_folder, fps=extraction_fps)
