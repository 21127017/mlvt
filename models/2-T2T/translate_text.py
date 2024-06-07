from google.cloud import translate_v2 as translate
import os

# Replace '/path/to/your/service-account-file.json' with the actual path to your service account JSON key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# Initialize the Google Cloud Translation client
translate_client = translate.Client()

# Define the paths
input_text_path = "../../data/output_S2T/transcript_test.txt"
input_name, _ = os.path.splitext(os.path.basename(input_text_path))
output_folder = "../../data/output_T2T"
output_text_file = os.path.join(output_folder, f"translated_{input_name}.txt")

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Read the text to be translated
with open(input_text_path, "r") as file:
    text_to_translate = file.read()

# Translate the text from English to French
translation = translate_client.translate(text_to_translate, target_language='fr')
translated_text = translation['translatedText']

# Save the translated text to a file
with open(output_text_file, "w") as file:
    file.write(translated_text)

print(f"Translated text saved to {output_text_file}")
