from moviepy.editor import VideoFileClip
import os
def crop_video(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    # Open the video clip using moviepy
    video_clip = VideoFileClip(video_path)
    fps = video_clip.fps
    total_duration = video_clip.duration
    chunk_duration = 600  # Chunk duration in seconds (e.g., 10 minutes)
    # Calculate the number of chunks
    num_chunks = int(total_duration // chunk_duration)
    for i in range(num_chunks):
        # Calculate start and end time for the chunk
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, total_duration)
        # Extract the video clip for the current chunk
        video_chunk = video_clip.subclip(start_time, end_time)
        # Write the video chunk to the output file
        output_path = os.path.join(output_folder, f"{i + 1}.mp4")
        video_chunk.write_videofile(output_path, codec="libx264", fps=fps)
    # Close the video clip
    video_clip.close()
if __name__ == "__main__":
    # Specify the input folder containing videos
    input_folder = r"C:\Users\ASDF\Desktop\anpr_dataset"
    # Specify the output base folder where folders for each video will be created
    output_base_folder = r"D:\code\annotations-conversion\chunks"
    # Process videos in the input folder
    for video_file in os.listdir(input_folder):
        if video_file.endswith(".mp4"):
            # Get the full path of the video
            video_path = os.path.join(input_folder, video_file)
            # Create a folder for each video in the output base folder
            output_folder = os.path.join(output_base_folder, os.path.splitext(video_file)[0])
            # Crop the video into chunks and save in the created folder
            crop_video(video_path, output_folder)