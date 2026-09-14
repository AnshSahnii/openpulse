# OpenPulse 🚀

## Open-source repository discovery, analysis, and bookmarking platform

OpenPulse is a full-stack web application designed to help users **discover, explore, analyze, and bookmark GitHub repositories** through a clean and structured dashboard.

The application combines a **React + TypeScript frontend**, **FastAPI backend**, **PostgreSQL database**, **SQLAlchemy**, **JWT authentication**, and the **GitHub REST API** to provide a complete repository discovery experience.

---

## ✨ Features

### 🔎 Repository Discovery

- Search GitHub repositories directly from the dashboard
- Explore repository metadata and key metrics
- View detailed repository information
- Retrieve repository data through the GitHub REST API
- Access recently viewed repository information

### 👤 User Authentication

- User registration
- User login
- JWT-based authentication
- Protected API endpoints
- Current-user profile endpoint
- Secure password handling

### 🔖 Personal Bookmarks

- Save repositories to a personal collection
- View bookmarked repositories
- Remove repositories from bookmarks
- Persist bookmark data in PostgreSQL

### ⚡ Performance & Backend

- Lightweight in-memory caching
- PostgreSQL-backed persistence
- Service and repository architecture
- Centralized error handling
- API pagination
- Structured API responses

### 🛠 Developer Experience

- RESTful API architecture
- Swagger/OpenAPI documentation
- Docker Compose support
- Alembic database migrations
- Automated backend tests
- Environment-based configuration

---

## 🖥️ Application Preview

<img width="1901" height="862" alt="Screenshot 2026-09-14 165454" src="https://github.com/user-attachments/assets/bbb00a57-29cd-4f01-ba97-9045ec0287bc" />

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      GitHub API     │
                    └──────────┬──────────┘
                               │
                               ▼
┌──────────────────┐     ┌──────────────────┐
│                  │     │                  │
│ React +          │────▶│ FastAPI REST API │
│ TypeScript       │     │                  │
│                  │◀────│                  │
└──────────────────┘     └────────┬─────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                    ▼             ▼             ▼
              ┌──────────┐ ┌──────────┐ ┌───────────┐
              │ Services │ │Repository│ │   Cache   │
              │          │ │   Layer  │ │           │
              └──────────┘ └────┬─────┘ └───────────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  PostgreSQL  │
                         └──────────────┘
```

### Request Flow

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Router
 │
 ▼
Service Layer
 │
 ├───────────────► GitHub REST API
 │
 └───────────────► Repository Layer
                         │
                         ▼
                     PostgreSQL
```

---

## 🧰 Technology Stack

### Frontend

| Technology | Purpose |
|------------|---------|
| React | User interface |
| TypeScript | Type-safe frontend development |
| Vite | Development and build tooling |
| CSS | Application styling |

### Backend

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database interaction |
| Pydantic | Data validation and schemas |
| JWT | Authentication |
| Alembic | Database migrations |

### Database & Infrastructure

| Technology | Purpose |
|------------|---------|
| PostgreSQL | Persistent application data |
| Docker | Containerization |
| Docker Compose | Multi-service environment |

### External Integration

| Technology | Purpose |
|------------|---------|
| GitHub REST API | Repository discovery and metadata |

---

## 📁 Project Structure

```text
OpenPulse/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── bookmarks.py
│   │   │       ├── health.py
│   │   │       ├── repositories.py
│   │   │       └── router.py
│   │   │
│   │   ├── core/
│   │   │   ├── cache.py
│   │   │   ├── error_handlers.py
│   │   │   ├── exceptions.py
│   │   │   ├── middleware.py
│   │   │   ├── pagination.py
│   │   │   └── security.py
│   │   │
│   │   ├── integrations/
│   │   │   └── github/
│   │   │       ├── client.py
│   │   │       ├── constants.py
│   │   │       └── schemas.py
│   │   │
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── migrations/
│   ├── tests/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── api.ts
│   │   ├── main.tsx
│   │   └── styles.css
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── docker-compose.yml
├── docker-compose.prod.yml
├── PROJECT.md
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.10+
- Node.js 18+
- PostgreSQL
- Git
- Docker Desktop *(optional)*

---

## ⚙️ Backend Setup

Navigate to the backend directory:

```powershell
cd backend
```

Create a Python virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install backend dependencies:

```powershell
pip install -r requirements.txt
```

Create your environment configuration:

```powershell
copy .env.example .env
```

Configure your PostgreSQL connection inside `.env`.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/openpulse
```

Create a PostgreSQL database named:

```text
openpulse
```

Run database migrations:

```powershell
alembic upgrade head
```

Start the FastAPI development server:

```powershell
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

---

## 🎨 Frontend Setup

Open a new terminal.

Navigate to the frontend directory:

```powershell
cd frontend
```

Install frontend dependencies:

```powershell
npm install
```

Start the Vite development server:

```powershell
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

---

## 🐳 Running with Docker

From the project root:

```bash
docker compose up --build
```

The application services will be started using Docker Compose.

### Frontend

```text
http://localhost:5173
```

### Backend

```text
http://localhost:8000
```

### Swagger API Documentation

```text
http://localhost:8000/docs
```

To stop the containers:

```bash
docker compose down
```

---

## 📚 API Documentation

OpenPulse provides interactive API documentation through Swagger/OpenAPI.

Once the backend is running, open:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation is available through:

```text
http://127.0.0.1:8000/redoc
```

The documentation provides an interactive interface for exploring and testing available API endpoints.

---

## 🔌 API Overview

OpenPulse exposes a versioned REST API under:

```text
/api/v1
```

### Authentication

#### Register

```http
POST /api/v1/auth/register
```

#### Login

```http
POST /api/v1/auth/login
```

#### Current User

```http
GET /api/v1/auth/me
```

### Repository Discovery

#### Search Repositories

```http
GET /api/v1/repositories/search?q=react
```

#### Repository Details

```http
GET /api/v1/repositories/{owner}/{repo}
```

#### Recent Repositories

```http
GET /api/v1/repositories/recent
```

### Bookmarks

#### Get Bookmarks

```http
GET /api/v1/bookmarks/
```

#### Add Bookmark

```http
POST /api/v1/bookmarks/{repository_id}
```

#### Remove Bookmark

```http
DELETE /api/v1/bookmarks/{repository_id}
```

---

## 🔐 Authentication Flow

OpenPulse uses JWT-based authentication for protected resources.

```text
┌─────────────────────┐
│   User Registration │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Authentication API  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      JWT Token      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Protected API      │
│     Requests        │
└─────────────────────┘
```

Protected endpoints require a valid authentication token.

---

## 🗄️ Database

OpenPulse uses **PostgreSQL** for persistent application data.

The backend uses:

- SQLAlchemy for ORM-based database interaction
- Alembic for database migrations
- Repository classes for database access
- Service classes for application and business logic

Run migrations using:

```bash
alembic upgrade head
```

---

## ⚡ Caching

OpenPulse includes a lightweight **in-memory caching layer** to reduce repeated external API requests and improve application responsiveness.

For production environments, this layer can be extended or replaced with a distributed caching solution such as Redis.

---

## 🧪 Testing

Backend tests are located in:

```text
backend/tests/
```

Run the test suite with:

```bash
cd backend
pytest
```

The project includes tests covering API functionality and security-related behavior.

---

## 🔒 Security & Configuration

Environment-specific configuration should be stored in `.env`.

Never commit real:

- Passwords
- API keys
- Database credentials
- JWT secrets
- Application secrets

Use:

```text
.env.example
```

as the template for local configuration.

Before production deployment:

- Replace development and default secrets
- Generate strong application secrets
- Use secure PostgreSQL credentials
- Enable HTTPS
- Configure production CORS policies
- Use a production-grade secret manager
- Run database migrations
- Disable development-only settings
- Review authentication and authorization configuration

---

## 🛣️ Future Improvements

Potential future enhancements include:

- Redis-based distributed caching
- Advanced repository filtering
- Repository comparison
- GitHub organization discovery
- Trending repository analytics
- User activity insights
- Advanced search and sorting
- Repository recommendation functionality
- Background synchronization jobs
- Production deployment and monitoring
- Expanded automated test coverage

---

## 🎯 What This Project Demonstrates

OpenPulse demonstrates practical experience with:

- Full-stack web application development
- REST API design
- React and TypeScript
- FastAPI and Python
- PostgreSQL
- SQLAlchemy ORM
- JWT authentication
- External API integration
- Service/repository architecture
- Database migrations
- API caching
- Docker and Docker Compose
- Automated testing
- Environment-based configuration

---

## 📌 Project Status

**Active Development**

OpenPulse currently provides:

- GitHub repository discovery
- Repository details
- User authentication
- Personal bookmarks
- Persistent database storage
- GitHub API integration
- API documentation
- In-memory caching
- Automated testing
- Docker support

---

## 👨‍💻 Author

### Ansh Sahni

Full-stack software engineering project focused on:

**API Development • External API Integration • Database Systems • Authentication • Modern Web Development**

---

## ⭐ Support

If you find OpenPulse useful, consider giving the repository a ⭐ on GitHub.
