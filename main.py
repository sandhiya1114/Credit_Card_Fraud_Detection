from fraud_engine.transaction_history import TransactionHistory
from fraud_engine.rule_engine import calculate_risk
from utils.helpers import load_transactions, log_fraud
from config.rules_config import FRAUD_RISK_THRESHOLD
from ml_engine.kmeans_detector import KMeansAnomalyDetector

def main():
    history = TransactionHistory()
    transactions = load_transactions("data/transactions.csv")

    # ML component
    ml_detector = KMeansAnomalyDetector()
    ml_detector.train(transactions[:3])  # minimal training

    for txn in transactions:
        risk, reasons = calculate_risk(txn, history)
        anomaly = ml_detector.is_anomaly(txn)

        if anomaly:
            reasons.append("ML anomaly detected")

        if risk >= FRAUD_RISK_THRESHOLD or anomaly:
            print("⚠ FRAUD DETECTED")
            print("Risk:", risk)
            for r in reasons:
                print("-", r)
            log_fraud(txn, risk, reasons)
        else:
            print("✅ SAFE TRANSACTION")

        history.add_transaction(txn)
        print("-" * 50)

if __name__ == "__main__":
    main()
