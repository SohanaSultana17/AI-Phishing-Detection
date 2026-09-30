import pandas as pd
import matplotlib.pyplot as plt
import joblib
import shap

# Load dataset
df = pd.read_csv("dataset/selected_features.csv")

# Separate features and target
X = df.drop("label", axis=1)
y = df["label"]

# Load trained model
model = joblib.load("model/phishing_model.pkl")

print("Model loaded successfully!")

# Use a small sample for SHAP
X_sample = X.sample(1000, random_state=42)

print("Creating SHAP explainer...")

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values
shap_values = explainer.shap_values(X_sample)

print("SHAP values calculated!")

# For binary classification, use the phishing class (label 0)
if isinstance(shap_values, list):
    phishing_shap = shap_values[0]
else:
    phishing_shap = shap_values[:, :, 0]

# Create SHAP summary plot
plt.figure()

shap.summary_plot(
    phishing_shap,
    X_sample,
    show=False
)

plt.title("SHAP Feature Importance - Phishing Detection")
plt.tight_layout()

plt.savefig(
    "model/shap_summary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSHAP analysis completed!")
print("Graph saved to: model/shap_summary.png")