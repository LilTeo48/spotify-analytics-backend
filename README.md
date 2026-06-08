# Spotify Analytics Backend

A backend analytics platform inspired by Spotify, built with FastAPI, SQLAlchemy, and PostgreSQL. The application provides RESTful APIs for managing artists, tracks, genres, and podcasts while exposing analytics-focused endpoints for search, rankings, and listening metrics.

## Features

### Core Functionality

* Artist Management
* Track Management
* Genre Management
* Podcast Management
* RESTful CRUD Operations
* FastAPI Swagger Documentation

### Analytics Features

* Search Podcasts by Name
* Top Podcasts by Hours Listened
* Health Check Endpoint
* Database Health Monitoring
* Listening Metrics and Reporting

### Engineering Features

* FastAPI Backend Architecture
* SQLAlchemy ORM
* PostgreSQL / SQLite Support
* Pydantic Data Validation
* Automated Testing with Pytest
* GitHub Actions CI/CD
* Modular Service Layer Design

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy

### Database

* PostgreSQL
* SQLite

### Testing

* Pytest

### DevOps

* Docker
* Docker Compose
* GitHub Actions

## API Endpoints

### Health

GET /health

GET /health/database

### Podcasts

POST /podcasts

GET /podcasts

PUT /podcasts/{podcast_name}

DELETE /podcasts/{podcast_name}

GET /search/podcasts?q={query}

GET /podcasts/top

### Example Top Podcasts Response

```json
[
  {
    "podcast_name": "Pardon My Take",
    "hours_listened": 120
  }
]
```

## Running the Application

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Running Tests

```bash
pytest
```

Current Test Status:

```text
14 passed
```

## Future Enhancements

* Dashboard Statistics Endpoint
* Top Artists Endpoint
* Top Tracks Endpoint
* User Listening Profiles
* Genre Analytics
* Authentication and Authorization
* Docker Deployment



## Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48


LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

