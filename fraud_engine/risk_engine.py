# fraud_engine/risk_engine.py

def calculate_risk(features):
    weights = [0.2, 0.2, 0.15, 0.15, 0.1, 0.1, 0.1]
    score = 0

    for f, w in zip(features, weights):
        score += f * w

    return min(int(score), 100)
