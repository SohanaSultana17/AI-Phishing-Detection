import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("dataset/selected_features.csv")

X = df.drop("label", axis=1)
y = df["label"]


# ==========================================
# 2. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# 3. CREATE MODELS
# ==========================================

models = {

    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            max_iter=1000,
            random_state=42
        ))
    ]),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42,
        max_depth=15
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
}


# ==========================================
# 4. TRAIN AND EVALUATE
# ==========================================

results = []

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        pos_label=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        pos_label=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        pos_label=0
    )

    results.append({
        "Model": name,
        "Accuracy": accuracy * 100,
        "Precision": precision * 100,
        "Recall": recall * 100,
        "F1-Score": f1 * 100
    })

    print("Accuracy :", f"{accuracy * 100:.2f}%")
    print("Precision:", f"{precision * 100:.2f}%")
    print("Recall   :", f"{recall * 100:.2f}%")
    print("F1-Score :", f"{f1 * 100:.2f}%")


# ==========================================
# 5. COMPARISON TABLE
# ==========================================

results_df = pd.DataFrame(results)

print("\n==========================================")
print("           MODEL COMPARISON")
print("==========================================")

print(
    results_df.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.2f}".format,
            "Precision": "{:.2f}".format,
            "Recall": "{:.2f}".format,
            "F1-Score": "{:.2f}".format
        }
    )
)

# Save results
results_df.to_csv(
    "dataset/model_comparison.csv",
    index=False
)

print("\nComparison saved to:")
print("dataset/model_comparison.csv")