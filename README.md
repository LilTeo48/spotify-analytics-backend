# Spotify Analytics Backend

A containerized REST API built with FastAPI, PostgreSQL, SQLAlchemy, Docker, and Docker Compose that provides Spotify-inspired analytics, search functionality, filtering, sorting, pagination, and CRUD operations.

The project demonstrates backend development, database management, API design, automated testing, and CI/CD workflows.

---

## Features

* CRUD operations for artists, tracks, and genres
* Analytics dashboard endpoints
* Search endpoints for artists, tracks, and genres
* Filtering support
* Sorting support
* Pagination support
* PostgreSQL database integration
* Docker containerization
* Docker Compose orchestration
* Automated testing with Pytest
* Continuous Integration with GitHub Actions

---

## Tech Stack

### Backend

* FastAPI
* Python 3.13

### Database

* PostgreSQL
* SQLAlchemy ORM

### DevOps

* Docker
* Docker Compose
* GitHub Actions

### Testing

* Pytest
* FastAPI TestClient

---

## API Endpoints

### Artists

```http
GET    /top-artists
POST   /top-artists
PUT    /top-artists/{artist_name}
DELETE /top-artists/{artist_name}
```

### Tracks

```http
GET    /top-tracks
POST   /top-tracks
PUT    /top-tracks/{track_name}
DELETE /top-tracks/{track_name}
```

### Genres

```http
GET    /top-genres
POST   /top-genres
PUT    /top-genres/{genre_name}
DELETE /top-genres/{genre_name}
```

### Search

```http
GET /search/artists
GET /search/tracks
GET /search/genres
```

### Analytics

```http
GET /analytics/dashboard
GET /analytics/counts
GET /analytics/top-artist
GET /analytics/top-track
GET /analytics/top-genre
GET /analytics/total-streams
GET /analytics/total-hours
GET /analytics/top-3-artists
GET /analytics/top-3-tracks
GET /analytics/top-3-genres
```

---

## Running with Docker

Build and start services:

```bash
docker compose up --build
```

Access Swagger UI:

```text
http://localhost:8000/docs
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Current Test Coverage:

* Dashboard endpoint
* Artist search endpoint
* Track search endpoint
* Genre search endpoint
* Artist filtering endpoint
* Track filtering endpoint
* Genre filtering endpoint
* Artist sorting endpoint
* Track sorting endpoint
* Genre sorting endpoint

Current Result:

```text
10 passed
```

---

## Continuous Integration

GitHub Actions automatically:

* Installs dependencies
* Runs Pytest
* Validates code on every push

Current CI Status:

✅ Passing

---

## Example Dashboard Response

```json
{
  "artist_count": 5,
  "track_count": 5,
  "genre_count": 3,
  "total_artist_streams": 5925,
  "total_track_streams": 2385,
  "total_hours_listened": 257,
  "top_artist": "Future",
  "top_track": "Blinding Lights",
  "top_genre": "Hip-Hop"
}
```

---

## Future Enhancements

* Deploy API to Render
* Expand automated test coverage
* Authentication and authorization
* Redis caching
* Advanced analytics endpoints
* Frontend dashboard integration
* Monitoring and logging


## Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48


LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

