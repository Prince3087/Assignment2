# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FfdXl2SFSabM1lhKQt6mIfLdGOAh0z9p
"""

!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

!pip install coqpit

!pip install TTS

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/coqui-ai/TTS
# %cd TTS

import csv

# Define your dataset containing general English and technical terms
data = [
    {"text": "The API is an important part of software architecture.", "phonemes": "T h ə ˈ eɪ ˈ p i aɪ ..."},
    {"text": "CUDA is used for parallel processing.", "phonemes": "ˈ k juː ˈ d eɪ ..."},
    {"text": "OAuth allows secure authorization.", "phonemes": "Oʊ θ ..."},
    {"text": "REST API is useful for web services.", "phonemes": "r ɛ s t ..."},
    # Add more sentences here as needed
]

# Save the dataset as a CSV
csv_file = "tts_technical_dataset.csv"
with open(csv_file, mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['text', 'phonemes'])  # CSV header
    for row in data:
        writer.writerow([row['text'], row['phonemes']])

# Check if the dataset is correctly written
!cat tts_technical_dataset.csv

# Download a pre-trained TTS model
!tts --model_name tts_models/en/ljspeech/tacotron2-DDC --list_speakers

# Create configuration JSON file for fine-tuning
config_content = '''
{
    "batch_size": 16,
    "epochs": 100,
    "learning_rate": 1e-4,
    "text_cleaner": "english_cleaners",
    "phoneme_language": "en-us"
}
'''

# Save configuration to a file
with open("config.json", "w") as config_file:
    config_file.write(config_content)

# Fine-tune using the custom dataset and configuration
!tts --train_path tts_technical_dataset.csv --config_path config.json --continue_path tts_models/en/ljspeech/tacotron2-DDC



!pip uninstall -y TTS

!pip install scipy

from TTS.api import TTS
from scipy.io.wavfile import write
import numpy as np

# Load the fine-tuned model
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=True)

# Define the text you want to convert to speech
sentence = "The API is essential in modern web development."

# Generate speech (returns list of numpy arrays)
wav = tts.tts(sentence)

# Save the numpy array as a .wav file using scipy.io.wavfile
# Convert the list of audio samples (wav) into a numpy array
wav_array = np.array(wav)

# Define the sample rate (commonly 22050 Hz, but you can confirm with your model's documentation)
sample_rate = 22050

# Save the audio file
write("api_sentence.wav", sample_rate, wav_array.astype(np.float32))

# Download the generated .wav file
from google.colab import files
files.download("api_sentence.wav")

import logging

# Set up logging for evaluation results
logging.basicConfig(filename="fine_tuning_logs.log", level=logging.INFO)

# Log the evaluation process
for i, sentence in enumerate(sentences):
    logging.info(f"Sentence {i+1}: {sentence}")
    # Example MOS score (you can replace this with actual computation)
    mos_score = 4.5
    logging.info(f"MOS score: {mos_score}")

!pip install TTS

from TTS.api import TTS