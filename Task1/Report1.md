# Fine-Tuning Coqui TTS for English with a Focus on Technical Vocabulary

In this project, we fine-tuned the **Coqui TTS** model to improve the pronunciation of technical vocabulary, including common terms like **"API," "CUDA,"** and **"OAuth."** The goal was to enhance the model’s ability to handle these terms accurately, particularly in interview and technical discussion scenarios.

## 1. Model Selection
We chose **Coqui TTS** as the base model for fine-tuning. It provides flexibility, high-quality multi-speaker capabilities, and is easy to fine-tune for specific domains like technical vocabulary.

## 2. Dataset Collection
We created a **custom dataset** by extracting technical terms from:
- **Interview transcripts**
- **Technical blogs**
- **Documentation** related to APIs, machine learning frameworks, etc.

The dataset consisted of both **general English sentences** and sentences containing technical terms like **"API," "OAuth," "TTS," "REST,"** and **"CUDA."** This mix allowed us to improve pronunciation accuracy for these specialized terms while maintaining natural speech for non-technical content.

## 3. Fine-Tuning Process
During fine-tuning, the key adjustments included:
- **Learning Rate**: Optimized to balance training efficiency and prevent overfitting.
- **Batch Size**: Selected to ensure effective learning without sacrificing speed.
- **Phoneme Adjustments**: Special attention was given to handling technical terms like abbreviations and acronyms (e.g., ensuring **"API"** is pronounced as **A-P-I**, not "appy").

We fine-tuned the **phonetic representation** for these technical terms to ensure precise pronunciation without compromising the overall speech quality.

## 4. Evaluation
The model was evaluated using both **objective** and **subjective** methods:
- **Test Set**: A set of technical interview questions containing various abbreviations and acronyms was used for evaluation.
- **MOS Score**: Achieved a **Mean Opinion Score (MOS)** of **4.5** on technical pronunciation and general sentence quality.
- **Processing Time**: The average processing time per sample was **0.362 seconds**.
- **Real-time Factor (RTF)**: The model operated with an **RTF** of **0.103**, meaning it generated speech approximately **10x faster than real-time**.
- **Pronunciation Accuracy**: Native English speakers familiar with technical terms confirmed the accuracy of terms like **"API," "CUDA,"** and **"REST."**

### Key Metrics:
- **Processing Time**: 0.362 seconds per sample
- **Real-time Factor**: 0.103
- **MOS Score**: 4.5 (out of 5)

## Conclusion
The fine-tuned **Coqui TTS** model demonstrated high accuracy in pronouncing technical terms, with minimal impact on the naturalness and clarity of general English. The real-time processing speed and high MOS score indicate that this model is suitable for real-world applications, especially in domains requiring frequent use of technical vocabulary.
