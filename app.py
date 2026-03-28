
import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

def text_preprocess(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

st.title("EDTECH Spam Shield")
try:
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('spam_model.pkl')
    user_input = st.text_area("Enter message:")
    if st.button("Predict"):
        data = tfidf.transform([user_input])
        prediction = model.predict(data)
        st.write(f"Result: {prediction[0]}")
except:
    st.error("Files missing!")
