import re
from urllib.parse import urlparse


def extract_url_features(url):
    """
    Extract features directly from a URL.
    """

    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path
    query = parsed.query

    # Remove port number
    domain_without_port = domain.split(":")[0]

    # Full URL
    full_url = url

    # URL length
    url_length = len(full_url)

    # Domain length
    domain_length = len(domain_without_port)

    # Check whether domain is an IP address
    is_domain_ip = 1 if re.match(
        r"^\d{1,3}(\.\d{1,3}){3}$",
        domain_without_port
    ) else 0

    # TLD length
    tld_length = 0

    if "." in domain_without_port:
        tld = domain_without_port.split(".")[-1]
        tld_length = len(tld)

    # Number of subdomains
    domain_parts = domain_without_port.split(".")

    if len(domain_parts) > 2:
        no_of_subdomain = len(domain_parts) - 2
    else:
        no_of_subdomain = 0

    # Obfuscation characters
    obfuscation_chars = ["@", "%"]

    no_of_obfuscated_char = sum(
        full_url.count(char)
        for char in obfuscation_chars
    )

    has_obfuscation = 1 if no_of_obfuscated_char > 0 else 0

    obfuscation_ratio = (
        no_of_obfuscated_char / url_length
        if url_length > 0 else 0
    )

    # Letters
    no_of_letters = sum(c.isalpha() for c in full_url)

    letter_ratio = (
        no_of_letters / url_length
        if url_length > 0 else 0
    )

    # Digits
    no_of_digits = sum(c.isdigit() for c in full_url)

    digit_ratio = (
        no_of_digits / url_length
        if url_length > 0 else 0
    )

    # Special characters
    no_of_equals = full_url.count("=")
    no_of_qmark = full_url.count("?")
    no_of_ampersand = full_url.count("&")

    special_characters = [
        "-", "_", ".", "/", ":", "@", "%", "#", "~"
    ]

    no_of_other_special_chars = sum(
        full_url.count(char)
        for char in special_characters
    )

    special_char_ratio = (
        no_of_other_special_chars / url_length
        if url_length > 0 else 0
    )

    # HTTPS
    is_https = 1 if parsed.scheme == "https" else 0

    features = {
        "URLLength": url_length,
        "DomainLength": domain_length,
        "IsDomainIP": is_domain_ip,
        "TLDLength": tld_length,
        "NoOfSubDomain": no_of_subdomain,
        "HasObfuscation": has_obfuscation,
        "NoOfObfuscatedChar": no_of_obfuscated_char,
        "ObfuscationRatio": obfuscation_ratio,
        "NoOfLettersInURL": no_of_letters,
        "LetterRatioInURL": letter_ratio,
        "NoOfDegitsInURL": no_of_digits,
        "DegitRatioInURL": digit_ratio,
        "NoOfEqualsInURL": no_of_equals,
        "NoOfQMarkInURL": no_of_qmark,
        "NoOfAmpersandInURL": no_of_ampersand,
        "NoOfOtherSpecialCharsInURL": no_of_other_special_chars,
        "SpacialCharRatioInURL": special_char_ratio,
        "IsHTTPS": is_https
    }

    return features


if __name__ == "__main__":

    test_url = "https://www.google.com"

    features = extract_url_features(test_url)

    print("\nExtracted URL Features:\n")

    for feature, value in features.items():
        print(f"{feature}: {value}")