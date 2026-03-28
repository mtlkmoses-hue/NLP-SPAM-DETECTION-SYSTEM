import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

# 1.  NLP data for the Cloud server
nltk.download('stopwords')

# 2. Preprocessing Function 
def text_preprocess(message):
    # Removed punctuation
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    # Removed stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# 3. App Interface
st.title("EDTECH Spam Shield")
st.markdown("---")

try:
    # 4. models
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('spam_model.pkl')
    
    user_input = st.text_area("Paste the message you want to check below:", height=150)
    
    if st.button("Analyze Message"):
        if user_input:
            # Transform and Predict
            data = tfidf.transform([user_input])
            prediction = model.predict(data)
            
            # Show Result
            if prediction[0] == 'spam':
                st.error("RESULT: THIS IS SPAM")
            else:
                st.success("RESULT: THIS IS A LEGITIMATE MESSAGE (HAM)")
        else:
            st.warning("Please enter a message first.")

except Exception as e:
    st.error("Error loading model files. Please ensure .pkl files are in the repository.")
