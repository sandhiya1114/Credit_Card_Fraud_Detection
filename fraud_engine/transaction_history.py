from datetime import timedelta

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_last_location(self):
        if not self.transactions:
            return None
        return self.transactions[-1]["location"]

    def get_recent_transactions(self, current_time, window_minutes):
        return [
            t for t in self.transactions
            if current_time - t["time"] <= timedelta(minutes=window_minutes)
        ]
