# Fine-tuning script for Coqui TTS on technical vocabulary

from TTS.utils.manage import ModelManager
from TTS.tts.models import TTS
from TTS.config import load_config
from TTS.utils.audio import AudioProcessor

# Step 1: Download and Load pre-trained TTS model
model_name = "tts_models/en/ljspeech/tacotron2-DDC"
manager = ModelManager()
model_path, config_path, _ = manager.download_model(model_name)

# Step 2: Load the configuration and initialize TTS model
config = load_config(config_path)
ap = AudioProcessor(**config.audio)
model = TTS(model_path, config_path)

# Step 3: Fine-tuning on technical terms dataset
model.fine_tune(dataset_path='path_to_your_dataset', 
                output_path='fine_tuned_model', 
                batch_size=32, 
                epochs=50, 
                lr=0.0001)

# Step 4: Save fine-tuned model and evaluate
model.save("fine_tuned_model")
test_sentence = "CUDA stands for Compute Unified Device Architecture."
model.tts_to_file(test_sentence, "cuda_output.wav")

# Evaluation
results = evaluate(fine_tuned_model, test_dataset)
print("MOS:", results['MOS'])
