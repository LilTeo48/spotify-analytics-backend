# Spotify Analytics Backend

A backend analytics API built with FastAPI, SQLAlchemy, and PostgreSQL that provides insights into Spotify listening data through ranking, aggregation, filtering, and analytics endpoints.

## Features

* FastAPI REST API
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Analytics Dashboard Endpoint
* Ranking Endpoints
* Aggregation Endpoints
* Filtering Endpoints
* Interactive Swagger Documentation

## Tech Stack

* Python 3
* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn
* Pydantic

## Project Structure

```text
spotify-analytics-backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone Repository

```bash
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
cd spotify-analytics-backend
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE spotify_analytics;
```

Update the database connection in `db.py`:

```python
DATABASE_URL = "postgresql://username@localhost:5432/spotify_analytics"
```

Run the API:

```bash
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Analytics Endpoints

### Dashboard

```http
GET /analytics/dashboard
```

### Counts

```http
GET /analytics/counts
```

### Total Streams

```http
GET /analytics/total-streams
```

### Total Hours

```http
GET /analytics/total-hours
```

## Ranking Endpoints

### Top Artist

```http
GET /analytics/top-artist
```

### Top Track

```http
GET /analytics/top-track
```

### Top Genre

```http
GET /analytics/top-genre
```

### Artist Rankings

```http
GET /analytics/artist-stream-ranking
```

### Track Rankings

```http
GET /analytics/track-stream-ranking
```

### Genre Rankings

```http
GET /analytics/genre-ranking
```

## Average Analytics

```http
GET /analytics/average-artist-streams
GET /analytics/average-track-streams
GET /analytics/average-genre-hours
```

## Lowest Analytics

```http
GET /analytics/least-streamed-artist
GET /analytics/least-streamed-track
GET /analytics/least-listened-genre
```

## Filtering Endpoints

### Filter Artists by Streams

```http
GET /top-artists?min_streams=1000
```

### Filter Tracks by Artist

```http
GET /top-tracks?artist=Future
```

### Filter Genres by Hours

```http
GET /top-genres?min_hours=50
```

## Example Response

```json
{
  "top_tracks": [
    {
      "id": 4,
      "track": "Mask Off",
      "artist": "Future",
      "streams": 465
    }
  ]
}
```

## Future Enhancements

* Pagination
* Sorting
* Search Endpoints
* Docker Support
* Authentication & Authorization
* Spotify API Integration
* Real User Listening Data
* Automated Testing
* CI/CD Pipeline

## Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48


LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

