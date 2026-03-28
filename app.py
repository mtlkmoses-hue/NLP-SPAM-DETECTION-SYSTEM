
import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def text_preprocess(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

st.title("BPC Spam Shield")

try:
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('spam_model.pkl')
    
    user_input = st.text_area("Enter message to analyze:")
    if st.button("Predict"):
        if user_input:
            data = tfidf.transform([user_input])
            prediction = model.predict(data)
            result = "SPAM" if prediction[0] == 'spam' else "Legitimate (Ham)"
            st.success(f"Result: {result}")
except Exception as e:
    st.error("Model files are loading...")
