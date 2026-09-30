# 🛡️ AI-Based Phishing URL Detection and Risk Analysis System

An AI-powered Machine Learning web application that analyzes URLs and predicts whether they are **Phishing** or **Legitimate**.

The system also provides a **phishing probability, risk score, risk level, and user-friendly explanations** based on suspicious URL characteristics.

The application is developed using **Python, Flask, Scikit-learn, and Random Forest** with an interactive web dashboard.

---

## 📌 Overview

Phishing is a common cybersecurity threat in which attackers use deceptive URLs to trick users into visiting malicious websites or revealing sensitive information.

This project aims to detect potentially phishing URLs using **Machine Learning and URL-based feature engineering**.

The system takes a URL as input, extracts structural characteristics from the URL, and passes these features to a trained Random Forest classifier.

### The system provides:

- 🔍 Phishing / Legitimate classification
- 📊 Phishing probability
- 🛡️ Risk score from 0–100
- ⚠️ Risk level
- 💡 Explanation of suspicious URL characteristics
- 📈 Machine Learning analysis and visualizations

> **Note:** The current system analyzes the URL string itself. It does not automatically open, crawl, or inspect the target website.

---

# 🎯 Objectives

The main objectives of this project are:

1. Detect potentially phishing URLs using Machine Learning.
2. Extract meaningful structural features from URLs.
3. Train and compare multiple classification models.
4. Use Random Forest for URL-based phishing detection.
5. Generate a probability-based risk score.
6. Provide understandable explanations for predictions.
7. Develop a user-friendly web interface using Flask.
8. Apply Explainable AI techniques for model analysis.

---

# ✨ Features

## 🔹 1. Phishing URL Detection

The user enters a URL and the system predicts:

```text
PHISHING
or

LEGITIMATE
🔹 2. Risk Score

The phishing probability is converted into a risk score between 0 and 100.

Risk Score	Risk Level
0–24	Low
25–49	Medium
50–74	High
75–100	Critical

The risk score is a model-derived indicator and is not a standardized cybersecurity risk rating.

🔹 3. URL Feature Extraction

The system extracts structural characteristics from the URL, including:

URL length
Domain length
IP address usage
TLD length
Number of subdomains
Obfuscation characters
Number of digits
Number of letters
Number of special characters
Query markers
HTTPS usage
Character ratios
🔹 4. Explainable Results

The application provides simple explanations based on URL characteristics.

Examples include:

URL is unusually long
URL uses an IP address instead of a normal domain
URL contains multiple subdomains
URL contains possible obfuscation characters
URL contains a high number of digits
URL contains a high proportion of special characters
URL does not use HTTPS
🔹 5. Machine Learning Analysis

The project includes:

Logistic Regression
Decision Tree
Random Forest
Feature importance analysis
SHAP analysis
Confusion matrix
Model comparison
🧠 System Architecture
                    ┌──────────────────────┐
                    │    User enters URL   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ URL Feature          │
                    │ Extraction           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Random Forest        │
                    │ Classifier           │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Phishing /      │        │ Phishing        │
        │ Legitimate      │        │ Probability     │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 └─────────────┬────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Risk Score &         │
                    │ Risk Level           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Explanation of URL   │
                    │ Characteristics      │
                    └──────────────────────┘
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Flask	Web application framework
Pandas	Data processing
NumPy	Numerical operations
Scikit-learn	Machine Learning
Random Forest	Classification
Matplotlib	Visualization
Seaborn	Data visualization
SHAP	Explainable AI
TLDExtract	URL/domain processing
HTML	Frontend structure
CSS	Frontend styling
Git	Version control
GitHub	Source code hosting
📊 Dataset

The project uses the PhiUSIIL Phishing URL Dataset from the UCI Machine Learning Repository.

The original dataset contains:

235,795 URL records
56 features
Binary classification labels
Label Mapping
0 → Phishing
1 → Legitimate

The dataset contains both phishing and legitimate URLs.

For the deployed application, a separate URL-only feature dataset was created so that predictions can be made directly from a URL entered by the user.

🔬 Machine Learning Methodology
1. Data Preprocessing

The dataset was analyzed for:

Missing values
Duplicate records
Class distribution
Relevant URL characteristics

The data was divided into training and testing sets using an 80:20 stratified split.

train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
2. Feature Engineering

The project initially analyzed a larger set of URL and webpage-related features.

For the deployed application, features that can be derived directly from the URL string were selected.

Important URL-based features include:

URLLength
DomainLength
IsDomainIP
TLDLength
NoOfSubDomain
HasObfuscation
NoOfObfuscatedChar
ObfuscationRatio
NoOfLettersInURL
LetterRatioInURL
NoOfDegitsInURL
DegitRatioInURL
NoOfEqualsInURL
NoOfQMarkInURL
NoOfAmpersandInURL
NoOfOtherSpecialCharsInURL
SpacialCharRatioInURL
IsHTTPS
🤖 Model Comparison

Three classification approaches were evaluated:

Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	99.97%	100.00%	99.93%	99.97%
Decision Tree	99.97%	99.96%	99.97%	99.96%
Random Forest	99.99%	100.00%	99.97%	99.98%

These results are based on the project's current dataset split.

A separate Random Forest model using only URL-derived features was trained for deployment in the Flask application.

📈 URL-Only Model Performance

The deployed application uses the URL-only Random Forest model.

Performance on the held-out test split:

Metric	Result
Accuracy	99.47%
Precision	99.76%
Recall	99.01%
F1 Score	99.38%
Confusion Matrix
                    Predicted
                 Phishing  Legitimate

Actual Phishing    19989       200
Actual Legitimate    48      26922

These results represent performance on the project's current train/test split. They should not be interpreted as guaranteed real-world phishing detection accuracy.

🔍 Explainable AI

The project includes feature importance analysis to understand which features contribute strongly to the trained model.

Some of the important features identified in the full-feature model include:

URL Similarity Index
Number of External References
HTTPS usage
Number of Other Special Characters
Number of Digits
Digit Ratio
URL Length
Letter Ratio

SHAP was also used for model-level explainability.

The generated SHAP visualization is available at:

model/shap_summary.png

The explanations displayed by the web application are rule-based URL characteristics, while SHAP is used separately for model-level analysis.

🌐 Web Application

The Flask application provides a simple interface where users can enter a URL.

Application Workflow
Enter URL
    ↓
Extract URL Features
    ↓
Random Forest Prediction
    ↓
Calculate Phishing Probability
    ↓
Generate Risk Score
    ↓
Determine Risk Level
    ↓
Display Explanation

The dashboard displays:

Analyzed URL
Prediction
Risk score
Risk level
Phishing probability
Legitimate probability
Analysis explanation
📁 Project Structure
AI_Phishing_Detection/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── dataset/
│   └── model_comparison.csv
│
├── model/
│   ├── phishing_model.pkl
│   ├── url_only_model.pkl
│   ├── confusion_matrix.png
│   ├── feature_importance.csv
│   ├── feature_importance.png
│   ├── model_comparison.png
│   └── shap_summary.png
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
└── utils/
    ├── __init__.py
    ├── compare_models.py
    ├── create_url_dataset.py
    ├── evaluate_model.py
    ├── explanations.py
    ├── feature_importance.py
    ├── feature_selection.py
    ├── predict.py
    ├── prepare_data.py
    ├── risk_score.py
    ├── shap_analysis.py
    ├── test_url_prediction.py
    ├── train_model.py
    ├── train_url_model.py
    └── url_features.py
⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/SohanaSultana17/AI-Phishing-Detection.git

Move into the project directory:

cd AI-Phishing-Detection
2. Create a Virtual Environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Flask Application
python app.py

Open the local address shown in the terminal, usually:

http://127.0.0.1:5000/
🧪 Example URLs
Legitimate Examples
https://www.google.com
https://www.microsoft.com
https://www.python.org
https://www.wikipedia.org
Suspicious-Looking Test Examples
http://192.168.1.100/login
http://secure-login-example.com/verify/account
http://login-example.com@192.168.1.100/signin

The suspicious examples above are synthetic test strings. They should not be visited.

📊 Generated Analysis Files

The project generates several analysis outputs.

Confusion Matrix
model/confusion_matrix.png

Used to visualize classification performance.

Feature Importance
model/feature_importance.png
model/feature_importance.csv

Shows the relative importance of features used by the model.

Model Comparison
model/model_comparison.png
dataset/model_comparison.csv

Used to compare different machine learning models.

SHAP Analysis
model/shap_summary.png

Provides model-level explainability using SHAP.

🔐 Security Considerations

The application analyzes URL strings without automatically visiting arbitrary websites.

This design avoids directly interacting with potentially malicious websites during prediction.

However, the output should be treated as an automated risk assessment, not definitive proof that a URL is safe or malicious.

Users should verify suspicious links using trusted security tools and sources before interacting with them.

⚠️ Limitations

The current implementation has several limitations:

It analyzes URL characteristics rather than the complete webpage.
It does not inspect webpage HTML or JavaScript.
It does not perform live WHOIS analysis.
It does not perform live DNS reputation analysis.
It does not automatically check domain reputation.
The risk score is a model-derived indicator rather than a standardized cybersecurity rating.
The explanations shown in the web interface are rule-based.
SHAP analysis is performed separately for model-level explainability.
Model performance is based on the available dataset and current train/test split.
The current random train/test split may not fully represent performance on previously unseen domains or future phishing campaigns.
🚀 Future Enhancements

Possible future improvements include:

Real-time domain reputation checking
DNS and WHOIS analysis
SSL certificate analysis
Website HTML analysis
JavaScript behavior analysis
Browser-based webpage inspection
Deep Learning-based phishing detection
Ensemble learning approaches
External validation using an independent dataset
Domain-grouped evaluation for better generalization testing
Real-time threat intelligence integration
Advanced Explainable AI dashboard
Continuous model retraining with new phishing data
🎓 Academic Project

This project was developed as a Computer Science and Engineering academic project with a focus on:

Machine Learning
Cybersecurity
URL Feature Engineering
Explainable AI
Flask Web Development
👩‍💻 Author

Sohana Sultana

Computer Science and Engineering
KIIT University

📜 Disclaimer

This project is intended for educational and research purposes.

A prediction from the system does not guarantee that a URL is malicious or safe. Users should not rely solely on this application when making security-sensitive decisions.

⭐ Project Highlights
🤖 Machine Learning-based phishing URL detection
🌐 Flask web application
🌲 Random Forest classification
🔍 URL feature engineering
📊 Risk scoring
💡 Explainable results
🧠 SHAP analysis
📈 Model comparison
📉 Confusion matrix
📊 Feature importance analysis
🛡️ Cybersecurity-focused application