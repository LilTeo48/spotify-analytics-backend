# Spotify Analytics Backend

A backend analytics platform inspired by Spotify, built with **FastAPI, SQLAlchemy, Pydantic, PostgreSQL, and SQLite**.

The application provides RESTful APIs for managing artists, tracks, genres, and podcasts while exposing analytics-focused endpoints for search, rankings, listening metrics, database summaries, validation, and health monitoring.

The project is designed as a backend-focused portfolio application demonstrating API development, relational database interaction, service-layer architecture, automated testing, error handling, validation, and containerized development.


**Tyler Chadwick**

GitHub:  
https://github.com/LilTeo48

LinkedIn:  
https://www.linkedin.com/in/tyler-chadwick-81b9a6275

Repository:  
https://github.com/LilTeo48/spotify-analytics-backend
---

## Features

### Core Functionality

- Artist Management
- Track Management
- Genre Management
- Podcast Management
- RESTful CRUD Operations
- Search Endpoints
- FastAPI Swagger Documentation
- ReDoc API Documentation
- Query Parameter Validation
- 404 Error Handling for Missing Resources
- Structured Pydantic Response Models

### Analytics Features

- Top Artist Analytics
- Top Track Analytics
- Top Genre Analytics
- Top 3 Artists
- Top 3 Tracks
- Top 3 Genres
- Artist Stream Rankings
- Track Stream Rankings
- Genre Rankings
- Average Artist Streams
- Average Track Streams
- Average Genre Listening Hours
- Least Streamed Artist
- Least Streamed Track
- Least Listened Genre
- Total Stream Metrics
- Total Listening Hours
- Database Counts
- Database Summary
- Listening Summary
- Top Podcasts by Hours Listened
- Search Artists
- Search Tracks
- Search Genres
- Search Podcasts
- API Health Check
- Database Health Monitoring

### Engineering Features

- FastAPI Backend Architecture
- SQLAlchemy ORM
- PostgreSQL / SQLite Support
- Pydantic Data and Response Validation
- FastAPI Query Validation
- Modular Route and Service Layer Design
- Automated Testing with Pytest
- FastAPI TestClient Integration
- CRUD Lifecycle Regression Testing
- Error-Handling Tests
- Query Validation Tests
- Analytics Endpoint Tests
- GitHub Actions CI/CD
- Docker Support
- Docker Compose Support
- Git-Based Development Workflow

---

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- PostgreSQL
- SQLite

### Testing

- Pytest
- FastAPI TestClient

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- Git
- GitHub

---

## Architecture Responsibilities

### `app/main.py`

- Initializes the FastAPI application
- Registers the application router
- Serves the backend API

### `app/routes/analytics.py`

- Defines HTTP endpoints
- Handles request and query validation
- Applies response models
- Converts missing-resource results into HTTP 404 responses
- Delegates business logic to the service layer

### `app/services/spotify_service.py`

- Handles database queries
- Implements CRUD operations
- Performs searching, filtering, and sorting
- Calculates analytics and rankings
- Returns structured service-layer responses

### `app/models/db_models.py`

- Defines SQLAlchemy database models
- Maps Python objects to relational database tables

### `app/models/schemas.py`

- Defines Pydantic request schemas
- Defines API response models
- Enforces structured API contracts

### `app/database/db.py`

- Configures the SQLAlchemy database engine
- Creates database sessions
- Provides database connectivity to the service layer

### `tests/test_api.py`

- Tests API endpoints using FastAPI TestClient
- Covers CRUD behavior
- Tests validation failures
- Tests 404 responses
- Tests analytics and database-summary endpoints

---

# API Endpoints

## Health

```text
GET /health
GET /health/database

# Project Architecture

```text
spotify-analytics-backend/
├── app/
│   ├── database/
│   │   └── db.py
│   ├── models/
│   │   ├── db_models.py
│   │   └── schemas.py
│   ├── routes/
│   │   └── analytics.py
│   ├── services/
│   │   └── spotify_service.py
│   └── main.py
├── tests/
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md



