# Spotify Analytics Backend

A FastAPI backend project that simulates Spotify streaming analytics through REST API endpoints. The application uses SQLite and SQLAlchemy to store and manage artist, track, and genre data while providing analytics insights through a RESTful API.

---

## Features

- REST API built with FastAPI
- SQLite database integration
- SQLAlchemy ORM for database operations
- CRUD operations for artists
- Analytics endpoints for artists, tracks, genres, and listening summaries
- Database seeding script for sample Spotify data
- Interactive Swagger/OpenAPI documentation
- Structured backend architecture following separation of concerns

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- REST APIs
- Git & GitHub

---

## Project Structure

```text
spotify-analytics-backend/
│
├── app/
│   ├── database/
│   │   ├── db.py
│   │   ├── init_db.py
│   │   └── seed_db.py
│   │
│   ├── models/
│   │   ├── schemas.py
│   │   └── db_models.py
│   │
│   ├── routes/
│   │   └── analytics.py
│   │
│   ├── services/
│   │   └── spotify_service.py
│   │
│   └── main.py
│
├── spotify_analytics.db
├── README.md
└── .gitignore
```

---

## Database Schema

### Artists

| Column | Type |
|----------|----------|
| id | Integer |
| artist | String |
| streams | Integer |

### Tracks

| Column | Type |
|----------|----------|
| id | Integer |
| track | String |
| artist | String |
| streams | Integer |

### Genres

| Column | Type |
|----------|----------|
| id | Integer |
| genre | String |
| hours_listened | Integer |

---

## API Endpoints

### Artists

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/top-artists` | Retrieve all artists |
| POST | `/top-artists` | Add a new artist |
| PUT | `/top-artists/{artist_name}` | Update an artist |
| DELETE | `/top-artists/{artist_name}` | Delete an artist |

### Tracks

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/top-tracks` | Retrieve all tracks |

### Genres

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/top-genres` | Retrieve all genres |

### Analytics

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/listening-summary` | Generate listening analytics summary |

---

## Example Responses

### Top Artists

```json
{
  "top_artists": [
    {
      "id": 1,
      "artist": "Drake",
      "streams": 1250
    },
    {
      "id": 2,
      "artist": "Kendrick Lamar",
      "streams": 980
    }
  ]
}
```

### Top Tracks

```json
{
  "top_tracks": [
    {
      "id": 1,
      "track": "HUMBLE.",
      "artist": "Kendrick Lamar",
      "streams": 420
    }
  ]
}
```

### Top Genres

```json
{
  "top_genres": [
    {
      "id": 1,
      "genre": "Hip-Hop",
      "hours_listened": 145
    }
  ]
}
```

### Listening Summary

```json
{
  "total_hours": 257,
  "favorite_artist": "Future",
  "favorite_genre": "Hip-Hop",
  "total_tracks_streamed": 2385,
  "total_artist_streams": 5925
}
```

---

## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
cd spotify-analytics-backend
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 3. Initialize the Database

```bash
python3 -m app.database.init_db
```

### 4. Seed the Database

```bash
python3 -m app.database.seed_db
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Once the server is running, open:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### OpenAPI JSON

```text
http://127.0.0.1:8000/openapi.json
```

---

## Skills Demonstrated

- Backend Development
- REST API Design
- Database Modeling
- SQLAlchemy ORM
- SQLite Database Management
- CRUD Operations
- Data Analytics Aggregation
- API Documentation
- Software Architecture
- Python Application Development

---

## Future Improvements

- PostgreSQL support
- Docker containerization
- Authentication and authorization
- Artist-to-track relationships using foreign keys
- Advanced analytics queries
- Search and filtering endpoints
- Unit and integration testing
- CI/CD pipeline with GitHub Actions

---

## Author

**Tyler Chadwick**

GitHub: https://github.com/LilTeo48

LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

