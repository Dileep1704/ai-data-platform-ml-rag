import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset
data = {
    "age": [22, 25, 30, 35, 40, 50],
    "salary": [20000, 30000, 50000, 60000, 80000, 90000],
    "target": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["age", "salary"]]
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "ml_service/model.pkl")

print("Model trained successfully!")