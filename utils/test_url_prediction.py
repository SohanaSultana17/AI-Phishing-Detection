import joblib
import pandas as pd

from url_features import extract_url_features


# Load trained URL-only model
model = joblib.load("model/url_only_model.pkl")

print("URL-only model loaded successfully!")


# Get URL from user
url = input("\nEnter a URL to test: ")

# Extract features
features = extract_url_features(url)

# Convert to DataFrame
X = pd.DataFrame([features])

# Make prediction
prediction = model.predict(X)[0]

# Get probability
probabilities = model.predict_proba(X)[0]

# Probability of phishing
phishing_probability = probabilities[
    list(model.classes_).index(0)
]

# Probability of legitimate
legitimate_probability = probabilities[
    list(model.classes_).index(1)
]


print("\n================================")
print("PHISHING DETECTION RESULT")
print("================================")

print("URL:", url)

if prediction == 0:
    print("Prediction: PHISHING")
else:
    print("Prediction: LEGITIMATE")

print(
    f"Phishing Probability: "
    f"{phishing_probability * 100:.2f}%"
)

print(
    f"Legitimate Probability: "
    f"{legitimate_probability * 100:.2f}%"
)