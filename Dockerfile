# Premier stade : construire les dépendances
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Deuxième stade : copier uniquement les fichiers nécessaires
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
