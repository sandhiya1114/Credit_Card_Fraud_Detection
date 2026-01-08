# train_model.py
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# -------------------------------
# Step 0: Ensure model folder exists
# -------------------------------
model_folder = "model"
if not os.path.exists(model_folder):
    os.makedirs(model_folder)
print(f"Model folder: {model_folder}")

# -------------------------------
# Step 1: Load dataset
# -------------------------------
data = pd.read_csv("dataset/transactions.csv")
print("Columns in dataset:", data.columns.tolist())
print("First 5 rows:\n", data.head())

# -------------------------------
# Step 2: Encode categorical columns
# -------------------------------
le_card = LabelEncoder()
le_merchant = LabelEncoder()

data['card_type_enc'] = le_card.fit_transform(data['card_type'])
data['merchant_enc'] = le_merchant.fit_transform(data['merchant'])

# -------------------------------
# Step 3: Features & target
# -------------------------------
feature_cols = ['amount', 'avg_spend', 'credit_limit', 'account_age', 'card_type_enc', 'merchant_enc']
X = data[feature_cols]
y = data['is_fraud']

# -------------------------------
# Step 4: Train-test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Step 5: Train Random Forest
# -------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(f"Model accuracy: {model.score(X_test, y_test)*100:.2f}%")

# -------------------------------
# Step 6: Save model & encoders
# -------------------------------
joblib.dump(model, os.path.join(model_folder, "fraud_model.pkl"))
joblib.dump(le_card, os.path.join(model_folder, "label_card.pkl"))
joblib.dump(le_merchant, os.path.join(model_folder, "label_merchant.pkl"))

print("✅ Model and encoders saved successfully!")
print("Files in model folder:", os.listdir(model_folder))

