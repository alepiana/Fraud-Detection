# 🛡️ Fraud Detection System

Un sistema di rilevamento frodi end-to-end basato su Machine Learning, servito tramite **FastAPI** e containerizzato con **Docker**.

## 🚀 Panoramica del Progetto
Il progetto analizza le transazioni finanziarie per identificare pattern sospetti. Include una pipeline di addestramento (Offline) e un'interfaccia API (Online) per ottenere previsioni in tempo reale.

## 🛠️ Stack Tecnologico
- **Linguaggio:** Python 3.12
- **Gestione Dipendenze:** [UV](https://astral.sh/uv) (Estremamente veloce)
- **Framework API:** [FastAPI](https://fastapi.tiangolo.com/)
- **Machine Learning:** Scikit-Learn (Random Forest), Joblib
- **Containerizzazione:** Docker & Docker Compose
- **Qualità del Codice:** Ruff (Linting), Mypy (Static Typing), Pre-commit

## 📂 Struttura della Repo
- `src/train.py`: Script per l'addestramento del modello.
- `src/main.py`: API server per le predizioni.
- `models/`: Contiene il modello addestrato (.joblib).
- `Dockerfile` & `docker-compose.yml`: Configurazione per il deploy.

## 🚦 Come Iniziare

### Prerequisiti
Assicurati di avere installato `uv` e `Docker`.
