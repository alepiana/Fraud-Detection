FROM python:3.11-slim

# 1. Installiamo UV nel container prendendolo dall'immagine ufficiale
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 2. Copiamo i file di configurazione di UV
COPY pyproject.toml uv.lock ./

# 3. Installiamo le dipendenze (senza installare il codice dell'app ancora)
# Questo crea un ambiente virtuale dentro il container
RUN uv sync --frozen --no-cache

# 4. Copiamo il resto delle cartelle (src, models, ecc.)
COPY . .

# 5. Eseguiamo il training (opzionale se hai già il modello, ma utile per test)
RUN uv run python src/train.py

# 6. Avviamo l'API
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]