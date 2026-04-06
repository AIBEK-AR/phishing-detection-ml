from model import train_model
from features import extract_features

model = train_model()

url = input("Введите URL: ")

features = extract_features(url)
result = model.predict([features])[0]

if result == 1:
    print("🚨 Фишинговый сайт!")
else:
    print("✅ Безопасный сайт")