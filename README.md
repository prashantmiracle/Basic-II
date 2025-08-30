# Fashion Forecasting Monorepo

This monorepo contains an AI-powered fashion demand forecasting platform for brands like **Studio Rama** and **Aayushmaa**. It includes a Next.js frontend, FastAPI backend with RQ workers, PostgreSQL database, Redis, and Nginx reverse proxy.

## Features
- User registration/login with JWT and Google OAuth placeholders
- Organization management with roles
- Sales CSV ingestion and signal placeholders
- Forecasting jobs using RQ and a basic time-series model
- PDF report generation
- Stripe/Razorpay billing stubs
- Docker Compose setup for local development

## Quickstart
```bash
# install python deps
cd apps/api
pip install -r requirements.txt

# run backend
uvicorn app.main:app --reload

# run frontend
cd ../web
npm install
npm run dev

# run tests
cd ../api
pytest
```

## Docker Compose
```bash
cp .env.example .env
docker compose up --build
```

The application will be available at `http://localhost:3000` with the API proxied at `/api`.

## License
MIT
