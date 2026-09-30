def calculate_risk_score(phishing_probability):
    """
    Convert phishing probability into a risk score from 0 to 100.
    """

    risk_score = round(phishing_probability * 100)

    if risk_score < 25:
        risk_level = "Low"

    elif risk_score < 50:
        risk_level = "Medium"

    elif risk_score < 75:
        risk_level = "High"

    else:
        risk_level = "Critical"

    return risk_score, risk_level


if __name__ == "__main__":

    # Test values
    test_probabilities = [
        0.10,
        0.30,
        0.60,
        0.90
    ]

    for probability in test_probabilities:

        score, level = calculate_risk_score(
            probability
        )

        print(
            f"Probability: {probability * 100:.0f}% "
            f"→ Risk Score: {score}/100 "
            f"→ Risk Level: {level}"
        )