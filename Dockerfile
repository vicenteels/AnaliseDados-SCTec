FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY POO/Main.py ./POO/Main.py
COPY POO/Arvore.py ./POO/Arvore.py
COPY POO/No.py ./POO/No.py

CMD ["python", "POO/Main.py"]
