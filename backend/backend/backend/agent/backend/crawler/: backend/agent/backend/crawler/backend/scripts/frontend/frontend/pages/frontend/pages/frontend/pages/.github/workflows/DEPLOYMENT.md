# Obesity Knowledge Base - Deployment Guide

## Architecture Overview

The system consists of three main components:

1. **Backend API** (FastAPI) - RAG engine + crawler management
2. **Frontend Dashboard** (Next.js/React) - Admin controls and Q&A chat
3. **Automated Crawler** (GitHub Actions) - Scheduled resource discovery

---

## Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp ../.env.example .env
# Edit .env and add your API keys

# Run API server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
