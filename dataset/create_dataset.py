import pandas as pd
import os

# Step 1: Make sure 'dataset' folder exists
if not os.path.exists("dataset"):
    os.makedirs("dataset")

# Step 2: Create sample data
data = {
    "amount": [500, 6000, 200, 1500, 8000],
    "avg_spend": [400, 700, 150, 1000, 600],
    "credit_limit": [1000, 5000, 500, 2000, 7000],
    "account_age": [12, 1, 24, 6, 2],  # in months
    "card_type": ["credit", "debit", "credit", "credit", "debit"],
    "merchant": ["Amazon", "Unknown", "Walmart", "eBay", "Unknown"],
    "is_fraud": [0, 1, 0, 0, 1]  # 1 = Fraud, 0 = Legit
}

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Save as CSV inside 'dataset' folder
df.to_csv("dataset/transactions.csv", index=False)

print("Dataset created successfully at 'dataset/transactions.csv'!")
print(df)
