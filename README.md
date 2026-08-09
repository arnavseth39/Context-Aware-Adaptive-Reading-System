# Context-Aware Adaptive Reading System

An AI-powered reading platform that enhances the digital reading experience by dynamically adapting music, visuals, and the user interface based on the narrative context of the text.

The system uses transformer-based Natural Language Processing (NLP) to analyze story content in real time and automatically classify passages into narrative categories such as **Action**, **Dialogue**, **Suspense**, and **Narrative**, creating a more immersive reading experience.

---

## Features

- Context-aware story analysis using NLP
- Real-time text classification with BART Zero-Shot Classification
- Interactive PDF reader
- Reading speed (WPM) calibration
- Dynamic music and UI adaptation
- Asynchronous inference pipeline
- Responsive React-based user interface

---

## Tech Stack

### Frontend
- React
- Vite
- HTML
- CSS
- PDF.js

### Backend / AI
- Python
- Hugging Face Transformers
- BART Large MNLI
- PyTorch

### Libraries
- Pandas
- NumPy
- Pygame

---

## System Workflow

1. User uploads a PDF.
2. Text is extracted page by page.
3. The text is preprocessed and divided into chunks.
4. A transformer model classifies each chunk into narrative categories.
5. The application dynamically updates:
   - Background music
   - UI appearance
   - Reading experience
6. The user can calibrate reading speed for smoother context transitions.

---

## Motivation

Traditional e-book readers provide the same reading experience regardless of the emotional context of the story.

This project explores how Artificial Intelligence can create a more immersive reading environment by combining Natural Language Processing with adaptive multimedia and user interaction.

---

## Future Improvements

- Train a custom deep learning model instead of zero-shot classification
- Personalized recommendation engine
- Emotion-aware soundtrack generation
- Multi-language support
- Cloud deployment
- LLM-powered summarization

---

## Skills Demonstrated

- Software Engineering
- React Development
- Python Programming
- Natural Language Processing
- Machine Learning
- Transformer Models
- Application Development
- Human-Computer Interaction
- Asynchronous Programming

---

## Author

**Arnav Seth**
