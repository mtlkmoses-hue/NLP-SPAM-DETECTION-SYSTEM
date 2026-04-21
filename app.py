
import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))

def text_preprocess(message):
    nopunc = ''.join([char for char in message if char not in string.punctuation])
    return [word for word in nopunc.split() if word.lower() not in stop_words]

st.title("EDTECH Spam Shield")
st.write("Professional security layer for communication.")

tfidf = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('spam_model.pkl')

user_input = st.text_area("Paste message here:")

if st.button("Check Message"):
    if user_input:
        data = tfidf.transform([user_input])
        prediction = model.predict(data)
        result = "SPAM" if prediction[0] == 1 else "SAFE (HAM)"
        st.subheader(f"Result: {result}")
