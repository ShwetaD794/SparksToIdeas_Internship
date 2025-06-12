# SparksToIdeas_Internship
# SparkToIdeas

# 🧠 Machine Learning Projects

## 🔬 1. Diabetes Prediction

## 📧 2. Email Spam Detection

This repository contains two machine learning projects built with *Random Forest Classifiers* and deployed using *Tkinter GUI*:

* *Diabetes Prediction*
* *Email Spam Detection*

Each project involves:

* Data preprocessing
* Model training
* Saving the model using joblib
* Developing a user-friendly GUI

---

## 📁 Directory Structure


.
├── Diabetes prediction/
│   ├── diabetes.csv              # Dataset
│   ├── diabetes_model.pkl        # Trained ML model
│   ├── scaler.pkl                # Scaler used in preprocessing
│   ├── GUI.py                    # GUI for prediction
│   └── main.py                   # Model training script
│
├── Spam Detection/
│   ├── spam.csv                  # Dataset
│   ├── spam_model.pkl            # Trained ML model
│   ├── vectorizer.pkl            # Text vectorizer
│   ├── gui.py                    # GUI for prediction
│   └── main.py                   # Model training script


---

## 🔬 Diabetes Prediction

### 📌 Description

This project uses patient health metrics to predict the likelihood of diabetes. The data is scaled, and a *RandomForestClassifier* is trained. The model and scaler are saved with joblib and loaded in a *Tkinter-based GUI* for easy predictions.

### 🚀 How to Run

1. Navigate to the project directory:

   bash
   cd "Diabetes prediction"
   

2. (Optional) Install required libraries:

   bash
   pip install scikit-learn pandas numpy tkinter joblib
   

3. Run the GUI:

   bash
   python GUI.py
   

---

## 📧 Email Spam Detection

### 📌 Description

This project classifies email messages as spam or not spam using *Natural Language Processing (NLP)* and a *Multinomial Naive Bayes classifier*. The text data is vectorized using CountVectorizer, and both the model and vectorizer are saved using joblib. The application is deployed in a *Tkinter GUI* for real-time classification.

### 🚀 How to Run

1. Navigate to the project directory:

   bash
   cd "Spam Detection"
   

2. (Optional) Install required libraries:

   bash
   pip install scikit-learn pandas numpy nltk joblib
   

3. Run the GUI:

   bash
   python gui.py
   

---

## 📦 Requirements

Here's a combined list of important libraries used:

txt
scikit-learn
pandas
numpy
joblib
nltk
tkinter (comes pre-installed with Python)

---

## 📚 Future Enhancements

* Add performance metrics (accuracy, precision, recall) in GUI
* Deploy as a web app using Flask or Streamlit
* Add logging and input validation

---

## 🙌 Author

Developed by Shweta Dhote
For suggestions, contributions, or questions, feel free to reach out!

---

