from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model/fraud_model.pkl")
le_card = joblib.load("model/label_card.pkl")
le_merchant = joblib.load("model/label_merchant.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    # Prepare dropdown options from encoders
    card_types = list(le_card.classes_)
    merchants = list(le_merchant.classes_)

    if request.method == "POST":
        amount = float(request.form['amount'])
        credit_limit = float(request.form['credit_limit'])
        account_age = int(request.form['account_age'])
        card_type_input = request.form['card_type']
        merchant_input = request.form['merchant']

        # Encode categorical inputs
        card_type_num = le_card.transform([card_type_input])[0]
        merchant_num = le_merchant.transform([merchant_input])[0]

        # Prepare features (without avg_spend)
        features = np.array([[amount, credit_limit, account_age, card_type_num, merchant_num]])
        pred = model.predict(features)[0]
        result = "Fraud" if pred == 1 else "Legitimate"

    return render_template("index.html", card_types=card_types, merchants=merchants, result=result)

if __name__ == "__main__":
    app.run(debug=True)
