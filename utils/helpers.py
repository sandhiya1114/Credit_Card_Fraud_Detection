import csv
from datetime import datetime

def load_transactions(csv_file):
    transactions = []
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append({
                "amount": float(row["amount"]),
                "location": row["location"],
                "time": datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
            })
    return transactions

def log_fraud(transaction, risk, reasons):
    with open("output/fraud_logs.txt", "a") as f:
        f.write(f"Transaction: {transaction}\n")
        f.write(f"Risk Score: {risk}\n")
        for r in reasons:
            f.write(f"- {r}\n")
        f.write("\n")
