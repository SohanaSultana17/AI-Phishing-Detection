import pandas as pd
import sys
import os

# Allow importing url_features.py from the same folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from url_features import extract_url_features


print("Loading original dataset...")

df = pd.read_csv("dataset/phishing_urls.csv")

print("Dataset loaded!")
print("Rows:", len(df))


# Extract URL features
print("\nExtracting URL features...")

features_list = []

for i, url in enumerate(df["URL"]):

    features = extract_url_features(str(url))
    features["label"] = df.iloc[i]["label"]

    features_list.append(features)

    if (i + 1) % 10000 == 0:
        print(f"Processed: {i + 1} URLs")


# Create new dataframe
url_df = pd.DataFrame(features_list)


# Save dataset
output_path = "dataset/url_only_features.csv"

url_df.to_csv(
    output_path,
    index=False
)


print("\n===================================")
print("URL-ONLY DATASET CREATED")
print("===================================")

print("Shape:", url_df.shape)

print("\nColumns:")
print(url_df.columns.tolist())

print("\nLabel distribution:")
print(url_df["label"].value_counts())

print("\nSaved to:")
print(output_path)