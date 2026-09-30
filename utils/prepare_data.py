import pandas as pd
from sklearn.model_selection import train_test_split

# Load selected dataset
df = pd.read_csv("dataset/selected_features.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Separate features and target
X = df.drop("label", axis=1)
y = df["label"]

print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n========== DATA SPLIT ==========")

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)

print("Training labels:", y_train.shape)
print("Testing labels:", y_test.shape)

print("\n========== TRAINING LABELS ==========")
print(y_train.value_counts())

print("\n========== TESTING LABELS ==========")
print(y_test.value_counts())