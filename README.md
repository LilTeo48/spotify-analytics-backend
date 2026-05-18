# Spotify Analytics Backend

A FastAPI backend project that simulates Spotify streaming analytics through REST API endpoints.

## Features

- Built REST APIs using FastAPI
- Structured backend architecture
- Interactive Swagger/OpenAPI documentation
- Simulated Spotify analytics data
- CRUD functionality for artists
- Clean separation of routes, services, models, and database logic

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- REST APIs
- Git & GitHub

---

## Project Structure

```bash
spotify-analytics-backend/
│
├── app/
│   ├── database/
│   │   └── db.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   └── analytics.py
│   │
│   ├── services/
│   │   └── spotify_service.py
│   │
│   └── main.py
│
├── README.md
└── .gitignore
