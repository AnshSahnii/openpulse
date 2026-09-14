# OpenPulse 🚀

OpenPulse is a full-stack open-source repository discovery dashboard built with React, TypeScript, FastAPI, PostgreSQL, SQLAlchemy and the GitHub REST API.

## Features
- GitHub repository search
- Repository details and metrics
- Persistent repository storage
- User registration and JWT authentication
- Personal bookmarks
- Recent repository feed
- Lightweight in-memory caching
- API documentation with Swagger/OpenAPI
- Docker Compose setup

## Run locally

### Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```
Backend: http://127.0.0.1:8000/docs

If using local PostgreSQL, create a database named `openpulse` and update `DATABASE_URL` in `.env` if your credentials differ.

### Frontend
```powershell
cd frontend
npm install
npm run dev
```
Frontend: http://localhost:5173

### Docker
From the project root:
```bash
docker compose up --build
```
Frontend: http://localhost:5173
Backend docs: http://localhost:8000/docs

## API highlights
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `GET /api/v1/repositories/search?q=react`
- `GET /api/v1/repositories/{owner}/{repo}`
- `GET /api/v1/repositories/recent`
- `GET /api/v1/bookmarks/`
- `POST /api/v1/bookmarks/{repository_id}`
- `DELETE /api/v1/bookmarks/{repository_id}`

## Architecture
```text
React + TypeScript
        |
     REST API
        |
      FastAPI
        |
    API Routes
        |
     Services
      /     \
GitHub     Repositories
 API           |
           PostgreSQL
```

For production, replace default secrets, use migrations (`alembic upgrade head`), put the API behind HTTPS, and configure a real secret manager.
