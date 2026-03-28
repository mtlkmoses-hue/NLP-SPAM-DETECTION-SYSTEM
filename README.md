# EDTECH Communication Spam Shield
Project 3: NLP-Spam Detection System

# Project Overview
This project addresses the security and efficiency of communications at EDTECH. Using Natural Language Processing (NLP) and Machine Learning, this system automatically classifies incoming messages as Ham (Legitimate) or Spam.

By filtering out marketing noise and potential phishing threats, The staff can focus on critical grid maintenance alerts and genuine customer service inquiries.

# Web Application
[Insert your Streamlit Link Here]

# Technical Workflow
Data Understanding: Analyzed a dataset of 5,572 messages identifying a clear correlation between message length and spam probability.

Preprocessing: Custom function to remove punctuation and English stopwords.

Vectorization: Implemented TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical features.

Model: Trained a Multinomial Naive Bayes classifier, achieving high accuracy and low false-positive rates.

Deployment: Built a user-friendly interface using Streamlit for real-time message analysis.

# Structure
Spam_Detection.ipynb: Full 11-step Data Science workflow.

app.py: Streamlit application code.

spam_model.pkl: The trained Naive Bayes model.

tfidf_vectorizer.pkl: The saved TF-IDF vectorizer.

requirements.txt: Necessary Python libraries.

# Product Thinking
This tool acts as a Digital Security Layer for edtech. It reduces the risk of corporate phishing and improves operational response times by prioritizing verified customer communications.

Your Final Step: requirements.txt
For this specific project, your requirements.txt file should contain:

Plaintext
streamlit
pandas
scikit-learn
joblib
nltk
