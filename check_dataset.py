import pandas as pd

# Load the dataset
data = pd.read_csv("dataset/transactions.csv")

# 1️⃣ Check all column names
print("Columns in dataset:", data.columns.tolist())

# 2️⃣ Check first 5 rows of the dataset
print("\nFirst 5 rows of dataset:")
print(data.head())

# 3️⃣ Check for missing values in 'card_type' and 'merchant'
if 'card_type' in data.columns:
    print("\nMissing values in 'card_type':", data['card_type'].isnull().sum())
else:
    print("\nColumn 'card_type' not found!")

if 'merchant' in data.columns:
    print("Missing values in 'merchant':", data['merchant'].isnull().sum())
else:
    print("Column 'merchant' not found!")
