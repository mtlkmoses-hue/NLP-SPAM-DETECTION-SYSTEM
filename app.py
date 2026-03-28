import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

# 1. Necessary NLP assets
@st.cache_resource
def download_nltk():
    nltk.download('stopwords')

download_nltk()

# 2. Preprocessing Function 
def text_preprocess(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# 3. App Interface
st.set_page_config(page_title="EDTECH Spam Shield", page_icon="🛡️")
st.title("EDTECH Spam Shield")
st.write("Detect whether a message is Spam or Legitimate (Ham).")

try:
    # 4. Load the saved model and vectorizer
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('spam_model.pkl')
    
    user_input = st.text_area("Paste message here:", height=150)
    
    if st.button("Analyze Message"):
        if user_input:
            # Transform text using the vectorizer
            data = tfidf.transform([user_input])
            prediction = model.predict(data)
            
            # Display results
            if prediction[0] == 'spam':
                st.error("RESULT: THIS IS SPAM")
            else:
                st.success("RESULT: THIS IS A LEGITIMATE MESSAGE (HAM)")
        else:
            st.warning("Please enter some text first.")

except Exception as e:
    st.error("Application is initializing or files are missing. Please ensure .pkl files are in the repository.")itory.")
