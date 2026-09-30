# 🛡️ AI-Based Phishing URL Detection and Risk Analysis System

An AI-powered machine learning web application that analyzes URLs and predicts whether they are **Phishing** or **Legitimate**. The system also provides a **phishing probability, risk score, risk level, and user-friendly explanations** based on suspicious URL characteristics.

The application is developed using **Python, Flask, Scikit-learn, and Random Forest** with an interactive web dashboard.

---

## 📌 Overview

Phishing is a common cybersecurity threat where attackers use deceptive URLs to trick users into visiting malicious websites or revealing sensitive information.

This project aims to detect potentially phishing URLs using Machine Learning and URL-based feature engineering.

The system takes a URL as input, extracts structural characteristics from the URL, and passes these features to a trained Random Forest classifier.

### The system provides:

- 🔍 Phishing / Legitimate classification
- 📊 Phishing probability
- 🛡️ Risk score from 0–100
- ⚠️ Risk level
- 💡 Explanation of suspicious URL characteristics
- 📈 Machine learning analysis and visualizations

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