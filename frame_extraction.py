import cv2
import os
def extract_frames(video_path, output_folder, fps=2):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    # Get total number of frames and frame rate of the video
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)
    # Calculate interval (in frames) to achieve desired fps
    frame_interval = int(frame_rate / fps)
    # Initialize frame count
    frame_count = 0
    # Read and save frames at the specified fps
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        if not ret:
            break  # Break loop if no frame is read
        # Check if the current frame should be saved (based on frame interval)
        if frame_count % frame_interval == 0:
            # Save the frame as an image file
            frame_output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_output_path, frame)
        # Increment frame count
        frame_count += 1
    # Release the video capture object
    video_capture.release()
    print(f"Frames extracted: {frame_count}")
    print(f"Frames saved at {fps} fps in: {output_folder}")
if __name__ == "__main__":
    # Specify input video file path
    input_video_path = r"D:\ubi\dataset\illegal_parking_video\Number Plate Identification Improperly parked SUV.mp4"
    # Specify output folder to save frames
    output_folder = r"D:\code\annotations-conversion\3"
    # Specify frame rate for frame extraction (frames per second)
    extraction_fps = 15
    # Extract frames from the video
    extract_frames(input_video_path, output_folder, fps=extraction_fps)