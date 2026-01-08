# utils/feature_engineering.py

def extract_features(tx, user_profile):
    amount = tx["amount"]
    hour = tx["hour"]

    # 1️⃣ Amount behavior
    amount_deviation = amount - user_profile["avg_amount"]
    high_amount = int(amount > user_profile["credit_limit"] * 0.8)

    # 2️⃣ Time behavior
    odd_time = int(hour < 5 or hour > 23)

    # 3️⃣ Frequency behavior
    rapid_tx = int(user_profile["tx_last_1hr"] > 3)

    # 4️⃣ Device behavior
    new_device = int(tx["device"] not in user_profile["known_devices"])

    # 5️⃣ Merchant behavior
    risky_merchant = int(tx["merchant"] in ["electronics", "travel"])

    return [
        amount,
        amount_deviation,
        high_amount,
        odd_time,
        rapid_tx,
        new_device,
        risky_merchant
    ]
