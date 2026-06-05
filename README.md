## Spotify Analytics Backend 

## Recent Updates

### PostgreSQL Migration

* Migrated the backend database from SQLite to PostgreSQL
* Updated SQLAlchemy configuration for PostgreSQL connectivity
* Seeded and verified data persistence using PostgreSQL
* Successfully validated all existing endpoints after migration

### Analytics Features

* Dashboard analytics endpoint
* Top artist, track, and genre analytics
* Average listening metrics
* Least streamed/listened metrics
* Ranking endpoints
* Top 3 artist, track, and genre endpoints

### Filtering Endpoints

Filter data using query parameters:

```http
GET /top-artists?min_streams=1000
GET /top-tracks?artist=Future
GET /top-genres?min_hours=50
```

### Pagination Support

Limit the number of results returned:

```http
GET /top-artists?limit=2
GET /top-tracks?limit=2
GET /top-genres?limit=2
```

### Current Project Statistics

* 35+ REST API Endpoints
* FastAPI Backend
* PostgreSQL Database
* SQLAlchemy ORM
* CRUD Operations
* Search Functionality
* Analytics Dashboard
* Ranking Metrics
* Filtering Support
* Pagination Support
* Interactive Swagger Documentation

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

## Upcoming Features

### Tier 6B – Sorting

```http
GET /top-artists?sort_order=asc
GET /top-artists?sort_order=desc

GET /top-tracks?sort_order=asc
GET /top-tracks?sort_order=desc

GET /top-genres?sort_order=asc
GET /top-genres?sort_order=desc
```

### Future Roadmap

* Sorting
* Advanced Search
* Docker Support
* Pytest Integration
* Spotify API Integration
* Authentication & Authorization
* CI/CD Pipeline
* Cloud Deployment

```
```

## Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48


LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

