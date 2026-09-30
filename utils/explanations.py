def generate_reasons(features):

    reasons = []

    # URL length
    if features["URLLength"] > 75:
        reasons.append(
            "URL is unusually long"
        )

    # IP address
    if features["IsDomainIP"] == 1:
        reasons.append(
            "URL uses an IP address instead of a normal domain name"
        )

    # Subdomains
    if features["NoOfSubDomain"] >= 3:
        reasons.append(
            "URL contains multiple subdomains"
        )

    # Obfuscation
    if features["HasObfuscation"] == 1:
        reasons.append(
            "URL contains possible obfuscation characters"
        )

    # Digits
    if features["NoOfDegitsInURL"] >= 5:
        reasons.append(
            "URL contains a high number of digits"
        )

    # Special characters
    if features["SpacialCharRatioInURL"] > 0.25:
        reasons.append(
            "URL contains a high proportion of special characters"
        )

    # Query parameters
    if features["NoOfQMarkInURL"] >= 2:
        reasons.append(
            "URL contains multiple query markers"
        )

    # HTTPS
    if features["IsHTTPS"] == 0:
        reasons.append(
            "URL does not use HTTPS"
        )

    # If no suspicious features found
    if len(reasons) == 0:
        reasons.append(
            "No major suspicious URL characteristics detected"
        )

    return reasons


if __name__ == "__main__":

    test_features = {
        "URLLength": 100,
        "IsDomainIP": 1,
        "NoOfSubDomain": 4,
        "HasObfuscation": 1,
        "NoOfDegitsInURL": 8,
        "SpacialCharRatioInURL": 0.35,
        "NoOfQMarkInURL": 2,
        "IsHTTPS": 0
    }

    reasons = generate_reasons(test_features)

    print("\nReasons:\n")

    for reason in reasons:
        print("⚠", reason)