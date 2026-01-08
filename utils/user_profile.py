# utils/user_profile.py

def get_user_profile(user_id):
    # Simulated user history (normally from DB)
    return {
        "user_id": user_id,
        "avg_amount": 3000,
        "credit_limit": 100000,
        "known_devices": ["mobile_1", "laptop_1"],
        "home_city": "Chennai",
        "tx_last_1hr": 1
    }


def get_last_transaction():
    return {
        "lat": 13.0827,      # Chennai
        "lon": 80.2707,
        "timestamp": 0       # simplified for demo
    }
