from sklearn.cluster import KMeans
import numpy as np

class KMeansAnomalyDetector:
    def __init__(self, n_clusters=2):
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.trained = False

    def train(self, transactions):
        X = np.array([[t["amount"]] for t in transactions])
        self.model.fit(X)
        self.trained = True

    def is_anomaly(self, transaction):
        if not self.trained:
            return False

        amount = np.array([[transaction["amount"]]])
        cluster = self.model.predict(amount)[0]
        center = self.model.cluster_centers_[cluster]

        distance = abs(amount[0][0] - center[0])

        return distance > 5000  # simple threshold

