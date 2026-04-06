import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    parsed = urlparse(url)

    # длина URL
    features.append(len(url))

    # длина домена
    features.append(len(parsed.netloc))

    # HTTPS
    features.append(1 if parsed.scheme == "https" else 0)

    # количество точек
    features.append(url.count("."))

    # есть цифры
    features.append(1 if re.search(r'\d', url) else 0)

    # подозрительные символы
    features.append(1 if "@" in url or "-" in url else 0)

    return features