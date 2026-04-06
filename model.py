import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from features import extract_features

def train_model():
    data = pd.read_csv("dataset.csv", sep=";")

    data.columns = data.columns.str.strip().str.lower()

    print(data.columns) 

    X = [extract_features(url) for url in data["url"]]
    y = data["label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model