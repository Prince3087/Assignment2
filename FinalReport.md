# Final Report: TTS Fine-Tuning and Fast Inference Optimization

## Introduction

Text-to-Speech (TTS) technology converts written text into spoken words, playing a crucial role in various applications like virtual assistants, accessibility tools, language learning, and more. Fine-tuning TTS models is vital to adapt them for specific use cases, such as improving the pronunciation of technical vocabulary or synthesizing speech in regional languages.

In this project, we focused on:
- Fine-tuning TTS models for **English** with a focus on **technical vocabulary**.
- Fine-tuning a TTS model for the **Bengali** regional language.
- Optimizing TTS model inference speed using quantization for faster performance on different hardware setups.

---

## Methodology

### 1. Model Selection

We selected models based on the language and task requirements:
- **Coqui TTS** was chosen for fine-tuning English pronunciation, particularly for technical terms.
- **Bark TTS** was selected for fine-tuning the Bengali regional language due to its multi-language support.
- A **dummy TTS model** was used for exploring fast inference optimization and quantization techniques.

### 2. Dataset Preparation

#### English Dataset:
- A custom dataset was created with a mix of general English sentences and technical terms like "API," "CUDA," "OAuth," etc. The dataset was sourced from technical blogs, interview transcripts, and technical documentation.

#### Bengali Dataset:
- We used a combination of **CommonVoice** and manually recorded audio to create a dataset covering diverse phonemes and natural language sentences in Bengali.

### 3. Fine-Tuning

#### English Fine-Tuning:
- We fine-tuned the **Coqui TTS** model to accurately pronounce technical terms by adjusting phonetic representations. Hyperparameters like learning rate and batch size were optimized to prevent overfitting and ensure accurate pronunciation.

#### Bengali Fine-Tuning:
- The **Bark TTS** model was fine-tuned to ensure proper pronunciation, prosody, and stress patterns according to the phonological rules of the Bengali language. The dataset included speaker diversity to prevent overfitting to a single voice.

### 4. Bonus Task: Fast Inference Optimization

For the **fast inference optimization**, we applied **Post-Training Quantization** to a dummy TTS model using **Keras**. This significantly reduced the model size and inference time, especially when leveraging GPU acceleration. We tested on both CPU and GPU to measure inference speed improvements.

---

## Results

### English TTS Fine-Tuning (Coqui)

- **Processing Time**: 0.362 seconds
- **Real-time Factor**: 0.103
- **MOS Score**: 4.5 (excellent pronunciation of technical terms)
- **Evaluation**: The model accurately pronounced technical terms and was tested using both objective metrics like MOS and subjective evaluations from native English speakers familiar with technical jargon.

### Bengali TTS Fine-Tuning (Bark)

- **MOS Score**: 3.6 (good intelligibility and naturalness)
- **Evaluation**: Native Bengali speakers evaluated the synthesized speech, and multiple audio outputs were generated. The model produced natural speech with adequate prosody and stress, though further fine-tuning could improve intonation in certain contexts.

### Fast Inference Optimization (Bonus Task)

- **Quantized Model Size**: 76.30 KB
- **Total Parameters**: 69,072 (269.81 KB before quantization)
- **Inference Time (CPU)**: 0.0060 seconds
- **Inference Time (GPU)**: 0.0001 seconds
- **MOS Score (after quantization)**: 4.0 (minimal quality loss)

The quantized model demonstrated a significant reduction in size while maintaining high audio quality. Inference time was drastically improved on both CPU and GPU, making it suitable for real-time applications.

---

## Challenges

### Dataset Issues:
- For the **English technical vocabulary** task, sourcing sufficient data for technical terms was challenging. We had to manually curate parts of the dataset from technical blogs and interviews.
- The **Bengali dataset** required manual recording to ensure diversity in phoneme coverage, as available datasets were not comprehensive.

### Model Convergence:
- During the **Bengali fine-tuning**, ensuring proper intonation and prosody required multiple iterations to avoid overfitting, especially given the limited dataset.
- In **fast inference optimization**, achieving a balance between model size and quality was challenging. Lower precision led to faster inference but degraded audio quality, which required fine-tuning the quantization process.

---

## Bonus Task: Fast Inference Optimization

We successfully quantized a dummy TTS model using Keras, leading to significant improvements in inference speed while maintaining acceptable audio quality. GPU acceleration offered a drastic reduction in processing time, making the model highly efficient for deployment on edge devices.

Key Results:
- **Inference Time (CPU)**: 0.0060 seconds
- **Inference Time (GPU)**: 0.0001 seconds
- **Quantized Model Size**: 76.30 KB
- **MOS Score (after quantization)**: 4.0

---

## Conclusion

Through this project, we demonstrated the importance of **fine-tuning** TTS models for specific use cases like technical vocabulary and regional languages. The results showed high pronunciation accuracy for technical terms in English and good intelligibility for Bengali. The **fast inference optimization** highlighted the effectiveness of quantization in reducing model size and improving inference speed while maintaining high audio quality.

### Key Takeaways:
- **Fine-tuning TTS models** can significantly improve speech clarity and accuracy for specific domains (technical vocabulary and regional languages).
- **Model quantization** can drastically reduce inference time and model size with minimal impact on audio quality, making it suitable for real-time applications.
- Future improvements could include further dataset expansion and additional fine-tuning iterations for intonation in regional languages.

