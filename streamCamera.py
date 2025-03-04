import os
import subprocess

# Configuration
rtsp_server_url = "rtsp://127.0.0.1:8554/stream"
video_device = "/dev/video0"

# Check if ffmpeg is installed
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
        print("FFmpeg is installed.")
    except FileNotFoundError:
        print("FFmpeg not found. Installing...")
        os.system("sudo apt update && sudo apt install -y ffmpeg")

# Start RTSP streaming with ffmpeg
def start_stream():
    try:
        print(f"Starting stream from {video_device} to {rtsp_server_url}...")
        subprocess.run(
            [
                "ffmpeg",
                "-f", "v4l2",               # Video4Linux2 for webcam
                "-i", video_device,         # Input device
                "-f", "rtsp",               # Output format
                rtsp_server_url             # RTSP server URL
            ]
        )
    except KeyboardInterrupt:
        print("Streaming stopped.")

# Main function
if __name__ == "__main__":
    check_ffmpeg()
    start_stream()
