from config.rules_config import *
from datetime import timedelta

def calculate_risk(transaction, history):
    risk_score = 0
    reasons = []

    if transaction["amount"] > AMOUNT_THRESHOLD:
        risk_score += RISK_HIGH_AMOUNT
        reasons.append("High transaction amount")

    last_location = history.get_last_location()
    if last_location and transaction["location"] != last_location:
        risk_score += RISK_LOCATION_CHANGE
        reasons.append("Location change detected")

    recent_txns = history.get_recent_transactions(
        transaction["time"], TIME_WINDOW_MINUTES
    )

    if len(recent_txns) >= MAX_TRANSACTIONS:
        risk_score += RISK_RAPID_TXN
        reasons.append("Too many transactions in short time")

    return risk_score, reasons
