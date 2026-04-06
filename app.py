from flask import Flask, request, jsonify, render_template
from model import train_model
from features import extract_features

app = Flask(__name__)
model = train_model()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data.get("url")
    features = extract_features(url)
    prediction = model.predict([features])[0]
    return jsonify({"url": url, "phishing": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
