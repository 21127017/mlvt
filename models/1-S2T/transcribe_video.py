import whisper
import os

# Load the Whisper model
model = whisper.load_model("base")

# Define the path to your video file and output text file
video_path = "../../data/input_S2T/test.mp4"
input_name, _ = os.path.splitext(os.path.basename(video_path))
output_folder = "../../data/output_S2T"
output_text_file = os.path.join(output_folder, f"transcript_{input_name}.txt")

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Transcribe the video file
result = model.transcribe(video_path)

# Save the transcription to a text file
with open(output_text_file, "w") as file:
    file.write(result["text"])

print(f"Transcription saved to {output_text_file}")
