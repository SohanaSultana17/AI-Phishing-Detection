import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("dataset/selected_features.csv")

X = df.drop("label", axis=1)
y = df["label"]


# ==========================================
# TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# TRAIN RANDOM FOREST
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("Training Random Forest...")

model.fit(X_train, y_train)

print("Training completed!")


# ==========================================
# PREDICTION
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# ==========================================
# SAVE CONFUSION MATRIX IMAGE
# ==========================================

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Phishing", "Legitimate"]
)

display.plot()

plt.title("Random Forest - Confusion Matrix")

plt.savefig(
    "model/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# MODEL COMPARISON GRAPH
# ==========================================

results = pd.read_csv("dataset/model_comparison.csv")

results.set_index("Model")[
    ["Accuracy", "Precision", "Recall", "F1-Score"]
].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Machine Learning Model Comparison")
plt.ylabel("Score (%)")
plt.xlabel("Model")
plt.ylim(95, 100.1)

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "model/model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGraphs saved successfully!")

print("1. model/confusion_matrix.png")
print("2. model/model_comparison.png")