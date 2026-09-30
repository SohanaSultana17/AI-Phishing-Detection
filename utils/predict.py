import joblib
import pandas as pd

from utils.url_features import extract_url_features
from utils.risk_score import calculate_risk_score
from utils.explanations import generate_reasons
# Load trained model
model = joblib.load("model/url_only_model.pkl")


def predict_url(url):

    # Extract URL features
    features = extract_url_features(url)

    # Convert features to DataFrame
    X = pd.DataFrame([features])

    # Make prediction
    prediction = model.predict(X)[0]

    # Get probabilities
    probabilities = model.predict_proba(X)[0]

    # Find probabilities using class labels
    phishing_probability = probabilities[
        list(model.classes_).index(0)
    ]

    legitimate_probability = probabilities[
        list(model.classes_).index(1)
    ]

    # Calculate risk
    risk_score, risk_level = calculate_risk_score(
        phishing_probability
    )

    # Prediction name
    if prediction == 0:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    # Generate explanations
    reasons = generate_reasons(features)

    return {
        "url": url,
        "prediction": result,
        "phishing_probability": phishing_probability,
        "legitimate_probability": legitimate_probability,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons,
        "features": features
    }


if __name__ == "__main__":

    print("===================================")
    print("AI PHISHING WEBSITE DETECTOR")
    print("===================================")

    url = input("\nEnter URL: ")

    result = predict_url(url)

    print("\n===================================")
    print("RESULT")
    print("===================================")

    print("URL:", result["url"])

    print(
        "Prediction:",
        result["prediction"]
    )

    print(
        f"Phishing Probability: "
        f"{result['phishing_probability'] * 100:.2f}%"
    )

    print(
        f"Legitimate Probability: "
        f"{result['legitimate_probability'] * 100:.2f}%"
    )

    print(
        f"Risk Score: "
        f"{result['risk_score']}/100"
    )

    print(
        f"Risk Level: "
        f"{result['risk_level']}"
    )

    print("\nWhy does this URL look suspicious?")

    for reason in result["reasons"]:
        print("⚠", reason)