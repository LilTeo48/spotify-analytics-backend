# Spotify Analytics Backend

A backend analytics platform inspired by Spotify, built with **FastAPI, SQLAlchemy, Pydantic, PostgreSQL, and SQLite**.

The application provides RESTful APIs for managing artists, tracks, genres, and podcasts while exposing analytics-focused endpoints for search, rankings, listening metrics, database summaries, validation, and health monitoring.

The project is designed as a backend-focused portfolio application demonstrating API development, relational database interaction, service-layer architecture, automated testing, error handling, validation, and containerized development.

**Tyler Chadwick**

GitHub:  
https://github.com/LilTeo48

LinkedIn:  
https://www.linkedin.com/in/tyler-chadwick-81b9a6275

**Repository:**  
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

## Project Architecture

text
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


Architecture Responsibilities
app/main.py
Initializes the FastAPI application
Registers the application router
Serves the backend API
app/routes/analytics.py
Defines HTTP endpoints
Handles request and query validation
Applies response models
Converts missing-resource results into HTTP 404 responses
Delegates business logic to the service layer
app/services/spotify_service.py
Handles database queries
Implements CRUD operations
Performs searching, filtering, and sorting
Calculates analytics and rankings
Returns structured service-layer responses
app/models/db_models.py
Defines SQLAlchemy database models
Maps Python objects to relational database tables
app/models/schemas.py
Defines Pydantic request schemas
Defines API response models
Enforces structured API contracts
app/database/db.py
Configures the SQLAlchemy database engine
Creates database sessions
Provides database connectivity to the service layer
tests/test_api.py
Tests API endpoints using FastAPI TestClient
Covers CRUD behavior
Tests validation failures
Tests 404 responses
Tests analytics and database-summary endpoints
API Endpoints
Health
GET /health
GET /health/database
API Health Check
GET /health

Example response:

{
  "status": "ok",
  "message": "Spotify Analytics API is running"
}
Database Health Check
GET /health/database

Verifies database connectivity from the application.

Artists
Get Top Artists
GET /top-artists

Supported query parameters:

min_streams
limit
sort_order

Example:

GET /top-artists?min_streams=1000&limit=5&sort_order=desc

Example response:

{
  "top_artists": [
    {
      "id": 1,
      "artist": "Future",
      "streams": 125000
    }
  ]
}
Add Artist
POST /top-artists

Example request:

{
  "artist": "Future",
  "streams": 125000
}
Update Artist
PUT /top-artists/{artist_name}
Delete Artist
DELETE /top-artists/{artist_name}
Search Artists
GET /search/artists?q={query}

Missing artists return:

404 Not Found
Tracks
Get Top Tracks
GET /top-tracks

Supported query parameters:

artist
limit
sort_order

Example:

GET /top-tracks?artist=Future&limit=5&sort_order=desc

Example response:

{
  "top_tracks": [
    {
      "id": 1,
      "track": "Example Track",
      "artist": "Future",
      "streams": 85000
    }
  ]
}
Add Track
POST /top-tracks

Example request:

{
  "track": "Example Track",
  "artist": "Future",
  "streams": 85000
}
Update Track
PUT /top-tracks/{track_name}
Delete Track
DELETE /top-tracks/{track_name}
Search Tracks
GET /search/tracks?q={query}

Missing tracks return:

404 Not Found
Genres
Get Top Genres
GET /top-genres

Supported query parameters:

min_hours
limit
sort_order

Example:

GET /top-genres?min_hours=50&limit=5&sort_order=desc

Example response:

{
  "top_genres": [
    {
      "id": 1,
      "genre": "Hip-Hop",
      "hours_listened": 240
    }
  ]
}
Add Genre
POST /top-genres

Example request:

{
  "genre": "Hip-Hop",
  "hours_listened": 240
}
Update Genre
PUT /top-genres/{genre_name}
Delete Genre
DELETE /top-genres/{genre_name}
Search Genres
GET /search/genres?q={query}

Missing genres return:

404 Not Found
Podcasts
Get All Podcasts
GET /podcasts
Add Podcast
POST /podcasts

Example request:

{
  "podcast_name": "Pardon My Take",
  "host": "Big Cat and PFT Commenter",
  "category": "Sports",
  "episodes": 250,
  "hours_listened": 120
}
Update Podcast
PUT /podcasts/{podcast_name}
Delete Podcast
DELETE /podcasts/{podcast_name}
Search Podcasts
GET /search/podcasts?q={query}
Top Podcasts
GET /podcasts/top

Example response:

[
  {
    "podcast_name": "Pardon My Take",
    "host": "Big Cat and PFT Commenter",
    "category": "Sports",
    "episodes": 250,
    "hours_listened": 120
  }
]

Missing podcasts return:

404 Not Found
Listening Analytics
Listening Summary
GET /listening-summary

Returns aggregate listening information including:

Total listening hours
Favorite artist
Favorite genre
Total streamed tracks
Top Analytics
Top Artist
GET /analytics/top-artist

Returns the artist with the highest stream count.

Top Track
GET /analytics/top-track

Returns the most-streamed track.

Top Genre
GET /analytics/top-genre

Returns the genre with the highest number of listening hours.

Top 3 Analytics
GET /analytics/top-3-artists
GET /analytics/top-3-tracks
GET /analytics/top-3-genres

Returns the three highest-ranked artists, tracks, and genres.

Average Analytics
Average Artist Streams
GET /analytics/average-artist-streams
Average Track Streams
GET /analytics/average-track-streams
Average Genre Hours
GET /analytics/average-genre-hours

These endpoints calculate average listening metrics across the stored data.

Least-Performing Analytics
Least Streamed Artist
GET /analytics/least-streamed-artist
Least Streamed Track
GET /analytics/least-streamed-track
Least Listened Genre
GET /analytics/least-listened-genre

These endpoints return the lowest-ranked item for each analytics category.

Rankings
Artist Stream Ranking
GET /analytics/artist-stream-ranking
Track Stream Ranking
GET /analytics/track-stream-ranking
Genre Ranking
GET /analytics/genre-ranking

Each endpoint returns ordered ranking data based on the relevant stream or listening metric.

Dashboard Analytics
GET /analytics/dashboard

Provides a high-level summary of the stored analytics data.

Example response:

{
  "artist_count": 10,
  "track_count": 25,
  "genre_count": 8,
  "total_artist_streams": 500000,
  "total_track_streams": 750000,
  "total_hours_listened": 420,
  "top_artist": "Future",
  "top_track": "Example Track",
  "top_genre": "Hip-Hop"
}
Database Analytics
Counts
GET /analytics/counts

Example response:

{
  "artist_count": 10,
  "track_count": 25,
  "genre_count": 8
}
Total Streams
GET /analytics/total-streams

Example response:

{
  "total_artist_streams": 500000,
  "total_track_streams": 750000,
  "combined_streams": 1250000
}
Total Listening Hours
GET /analytics/total-hours

Example response:

{
  "total_hours_listened": 420
}
Database Summary
GET /analytics/database-summary

Example response:

{
  "artist_count": 10,
  "track_count": 25,
  "genre_count": 8,
  "podcast_count": 5
}
Validation and Error Handling
Limit Validation
1 <= limit <= 100

Invalid limits return:

422 Unprocessable Entity
Minimum Stream Validation
min_streams >= 0

Negative values are rejected automatically.

Minimum Hours Validation
min_hours >= 0

Negative values are rejected automatically.

Sort Order Validation

Accepted values:

asc
desc

Invalid values return:

422 Unprocessable Entity
Missing Resources

Update and delete operations return proper HTTP 404 responses when a resource does not exist.

Example:

{
  "detail": "Artist not found"
}
Running the Application
1. Clone the Repository
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
cd spotify-analytics-backend
2. Create a Virtual Environment
python3 -m venv .venv

Activate on macOS/Linux:

source .venv/bin/activate

Activate on Windows:

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Start the Application
uvicorn app.main:app --reload

Application:

http://127.0.0.1:8000
API Documentation
Swagger UI
http://127.0.0.1:8000/docs
ReDoc
http://127.0.0.1:8000/redoc
Testing

The project includes automated API tests using Pytest and FastAPI TestClient.

Run the test suite:

pytest

Current test status:

38 passed
Test Coverage

The automated suite covers:

Health endpoints
Database health
Artist endpoints
Track endpoints
Genre endpoints
Podcast endpoints
Search behavior
Filtering
Sorting
Limits
Query validation
Invalid sort-order handling
Missing-resource 404 behavior
Artist CRUD lifecycle
Track CRUD lifecycle
Genre CRUD lifecycle
Podcast CRUD lifecycle
Top podcast response structure
Analytics endpoints
Rankings
Database summaries
Stream metrics
Listening-hour metrics
CRUD Lifecycle Testing

CRUD regression tests create uniquely named temporary resources using UUID values.

Each lifecycle test:

Creates a temporary resource.
Verifies successful creation.
Updates the resource.
Verifies the updated values.
Deletes the resource.

This keeps the tests from depending on pre-existing database records.

Continuous Integration

The project uses GitHub Actions for automated CI testing.

The CI workflow is designed to run the test suite when code changes are pushed or submitted through pull requests.

This helps catch regressions before changes are merged into the main branch.

Docker

The project includes Docker and Docker Compose support.

Build the image:

docker build -t spotify-analytics-backend .

Run the container:

docker run -p 8000:8000 spotify-analytics-backend

Docker Compose can also be used to run the API alongside PostgreSQL.

Production-style Docker and PostgreSQL verification will be completed during the final hardening stage.

Database Support

The application supports:

SQLite for local development
PostgreSQL for production-style environments

SQLAlchemy provides the ORM layer between FastAPI and the configured relational database.

The local SQLite database is intentionally excluded from Git tracking.

Repository Hygiene

Ignored local artifacts include:

.venv/
.env
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
spotify_analytics.db
Future Enhancements
Authentication and Authorization
User Accounts
User Listening Profiles
Spotify Web API Integration
OAuth Integration
Pagination Metadata
Advanced Filtering
Alembic Database Migrations
Production Hosting
Frontend Analytics Dashboard
API Rate Limiting
Logging and Observability
Additional Integration Tests
Cloud Deployment
Project Goals

This project demonstrates:

REST API development
SQLAlchemy ORM usage
Relational database operations
CRUD API design
Pydantic schemas
FastAPI response models
Service-layer architecture
Query validation
HTTP error handling
Search and filtering
Analytics development
Ranking logic
Automated regression testing
CI/CD practices
Docker-based development
PostgreSQL integration
Git and GitHub workflows


├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
