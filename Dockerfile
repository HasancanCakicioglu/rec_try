# İlk aşama: Gerekli bağımlılıkları yükle
FROM python:3.9 AS builder

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# İkinci aşama: Uygulama dosyalarını kopyala
FROM python:3.9-slim

WORKDIR /code

COPY --from=builder /code /code

COPY ./src /code/app

# Docker içinde çalışacak komutu belirle
CMD ["python3", "app/main.py"]
