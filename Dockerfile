FROM python:3.11-slim

# Evita logs bufferizados
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Seguridad básica
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn", "--workers=2", "--threads=2", "--bind=0.0.0.0:5000", "run:app"]