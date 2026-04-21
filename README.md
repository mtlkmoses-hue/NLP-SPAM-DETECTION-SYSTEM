# EDTECH Spam Shield – SMS Spam Detection System

## Overview
EDTECH Spam Shield is a machine learning-based application that detects whether a message is **Spam or Ham (Safe)**.  
It uses Natural Language Processing (NLP) techniques and a Naive Bayes classifier trained on SMS data.

The system is deployed using **Streamlit** for a simple and interactive user interface.
# Web Application
(https://nlp-spam-detection-system.streamlit.app/)

## Features
- Text preprocessing (punctuation removal, stopword filtering)
- TF-IDF vectorization for text feature extraction
- Machine learning classification using Multinomial Naive Bayes
- Real-time spam detection via Streamlit web app
- Model and vectorizer saved for reuse (`.pkl` files)

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib

## Dataset
The model is trained on an SMS spam dataset containing labeled messages:
- **Ham (0)** → Normal messages  
- **Spam (1)** → Unwanted messages


## Installation

1. Clone the repository:
git clone https://github.com/mtlkmoses-hue/NLP-SPAM-DETECTION-SYSTEM

