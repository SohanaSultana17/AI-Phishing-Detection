import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load dataset
df = pd.read_csv("dataset/selected_features.csv")

# Separate features
X = df.drop("label", axis=1)

# Load trained model
model = joblib.load("model/phishing_model.pkl")

# Get feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

# Sort from highest to lowest
importance = importance.sort_values(
    by="Importance",
    ascending=False
)

# Display top 15 features
print("\n========== TOP 15 IMPORTANT FEATURES ==========\n")
print(importance.head(15).to_string(index=False))

# Save feature importance data
importance.to_csv(
    "model/feature_importance.csv",
    index=False
)

# Select top 15 for graph
top_features = importance.head(15).sort_values(
    by="Importance"
)

# Create graph
plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")

plt.tight_layout()

# Save graph
plt.savefig(
    "model/feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nFeature importance saved successfully!")
print("1. model/feature_importance.csv")
print("2. model/feature_importance.png")