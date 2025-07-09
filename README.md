# sms-spam-classifier
A machine learning model to detect SMS spam using Python and NLP


# 📩 SMS Spam Classifier

An intelligent SMS Spam Classifier built using Python, Machine Learning, and Natural Language Processing (NLP). This model detects whether a given SMS is **spam** or **ham** (not spam) with high accuracy.

---

## 🚀 Features

- Detects spam vs. ham messages using NLP
- Text preprocessing: stopwords removal, stemming, lowercase transformation
- ML model: Multinomial Naive Bayes
- Streamlit web interface (optional)
- Trained on SMS Spam Collection Dataset

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn**
- **NLTK**
- **Pandas, NumPy**
- **Streamlit** (for GUI – optional)

---

## 📂 Project Structure


---

## 📊 Model Workflow

1. Load and clean SMS dataset  
2. Preprocess text data (tokenization, stopwords removal, etc.)  
3. Convert text to numerical features using CountVectorizer or TfidfVectorizer  
4. Train Naive Bayes classifier  
5. Predict spam/ham  
6. (Optional) Build a GUI using Streamlit

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier
pip install -r requirements.txt

📁 Dataset Source
UCI SMS Spam Collection Dataset

▶️ Run the App
To run the script:
python app.py
If using Streamlit:
streamlit run app.py

💡 Future Improvements
Deploy as a web app or mobile app

Add deep learning model (LSTM) for better accuracy

Real-time SMS input via mobile API

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
