import streamlit as st
import pickle

# Load model and vectorizer
model, tfidf = pickle.load(open("model.pkl", "rb"))

# Text cleaning
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

nltk.download('stopwords')
def clean_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c not in string.punctuation)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

# Streamlit UI
st.title("📩 SMS Spam Classifier")

msg = st.text_area("Enter your message")

if st.button("Classify"):
    cleaned = clean_text(msg)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)[0]
    if prediction == 1:
        st.error("🚨 Spam Message Detected!")
    else:
        st.success("✅ Not Spam (Ham)")
