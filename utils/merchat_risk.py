# Merchant risk profile (simulated)
MERCHANT_RISK = {
    "Amazon": 10,
    "Flipkart": 10,
    "Swiggy": 5,
    "Zomato": 5,
    "LocalShop": 15,
    "Unknown": 25
}

BLACKLISTED_MERCHANTS = ["FraudMart", "ScamStore"]

def get_merchant_risk(name):
    if name in BLACKLISTED_MERCHANTS:
        return 100  # direct fraud
    return MERCHANT_RISK.get(name, 20)
