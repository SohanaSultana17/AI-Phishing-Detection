import pandas as pd

# Load dataset
df = pd.read_csv("dataset/phishing_urls.csv")

# Features selected for the machine learning model
selected_features = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "URLSimilarityIndex",
    "CharContinuationRate",
    "TLDLegitimateProb",
    "URLCharProb",
    "TLDLength",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "ObfuscationRatio",
    "NoOfLettersInURL",
    "LetterRatioInURL",
    "NoOfDegitsInURL",
    "DegitRatioInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "NoOfOtherSpecialCharsInURL",
    "SpacialCharRatioInURL",
    "IsHTTPS",
    "NoOfURLRedirect",
    "NoOfSelfRedirect",
    "HasExternalFormSubmit",
    "HasPasswordField",
    "Bank",
    "Pay",
    "Crypto",
    "NoOfExternalRef",
    "label"
]

# Create new dataset
selected_df = df[selected_features]

# Save cleaned dataset
selected_df.to_csv(
    "dataset/selected_features.csv",
    index=False
)

print("Feature selection completed!")
print("Original dataset shape:", df.shape)
print("New dataset shape:", selected_df.shape)

print("\nSelected features:")
for feature in selected_features:
    print("-", feature)

print("\nLabel distribution:")
print(selected_df["label"].value_counts())
