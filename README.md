# TTS Fine-Tuning and Fast Inference Optimization

## Overview

This repository contains the implementation of three main tasks focused on improving Text-to-Speech (TTS) models. The tasks were assigned during my internship at **Parimal Lab, IIT Roorkee**, with a focus on fine-tuning TTS for specific applications and optimizing inference speed.

### Tasks Overview:

1. **Fine-Tuning TTS for English Technical Vocabulary**
2. **Fine-Tuning TTS for Bengali Regional Language**
3. **Fast Inference Optimization for a Dummy TTS Model**

---

## Task 1: Fine-Tuning TTS for English Technical Vocabulary

In this task, I fine-tuned the **Coqui TTS** model to enhance the pronunciation of technical terms used in interviews. 

### Steps:
- **Model Selection**: Chose Coqui TTS for its multi-speaker capabilities.
- **Dataset Preparation**: Created a dataset combining general English sentences and technical terms sourced from interview transcripts and technical blogs.
- **Fine-Tuning**: Adjusted phonetic representations and optimized hyperparameters to improve pronunciation accuracy.
- **Evaluation**: Measured performance using Mean Opinion Score (MOS), achieving a score of **4.5**.

---

## Task 2: Fine-Tuning TTS for Bengali Regional Language

This task involved fine-tuning the **Bark TTS** model for the Bengali language to synthesize natural speech.

### Steps:
- **Model Selection**: Selected Bark TTS for its capability to support multiple languages.
- **Dataset Preparation**: Sourced data from **CommonVoice** and recorded additional samples to cover diverse phonemes.
- **Fine-Tuning**: Focused on prosody, stress patterns, and pronunciation aligned with Bengali phonological rules.
- **Evaluation**: Conducted tests with native speakers, resulting in a MOS score of **3.6**.

---

## Task 3: Fast Inference Optimization

In the final task, I implemented fast inference optimization on a dummy TTS model using **Keras**.

### Steps:
- **Model Quantization**: Applied Post-Training Quantization to reduce model size from **269.81 KB** to **76.30 KB**.
- **Inference Optimization**: Tested the optimized model on CPU and GPU, measuring significant improvements in inference speed.
- **Evaluation**: The quantized model maintained a high MOS score of **4.0**, demonstrating minimal quality loss.

---

## Challenges Encountered

Throughout the project, I faced challenges such as:
- Sourcing comprehensive datasets for both English technical terms and Bengali speech.
- Model convergence issues during fine-tuning, especially for the Bengali TTS model.

These challenges enhanced my understanding of TTS model customization and the importance of dataset quality.

---

## Conclusion

This internship at Parimal Lab, IIT Roorkee, provided valuable experience in TTS technology. The results highlighted the potential of fine-tuning models for specific applications and the effectiveness of quantization techniques for optimizing performance. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

Special thanks to **Parimal Lab, IIT Roorkee**, for the opportunity and support throughout this internship.
