# Spotify Analytics Backend

A backend API built with FastAPI, SQLAlchemy, and SQLite that simulates Spotify listening analytics. The application provides CRUD operations for artists, tracks, and genres while generating listening insights through aggregated analytics endpoints.

## Features

### Artist Management

* Create artists
* Read artist data
* Update artist information
* Delete artists

### Track Management

* Create tracks
* Read track data
* Update track information
* Delete tracks

### Genre Management

* Create genres
* Read genre data
* Update genre information
* Delete genres

### Listening Analytics

* Top Artists
* Top Tracks
* Top Genres
* Listening Summary
* Favorite Artist Calculation
* Favorite Genre Calculation
* Total Listening Hours
* Total Track Streams
* Total Artist Streams

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* REST APIs
* Git & GitHub

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
│   │   ├── db_models.py
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
├── spotify_analytics.db
├── requirements.txt
└── README.md
```

## API Endpoints

### Artists

| Method | Endpoint                   |
| ------ | -------------------------- |
| GET    | /top-artists               |
| POST   | /top-artists               |
| PUT    | /top-artists/{artist_name} |
| DELETE | /top-artists/{artist_name} |

### Tracks

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /top-tracks              |
| POST   | /top-tracks              |
| PUT    | /top-tracks/{track_name} |
| DELETE | /top-tracks/{track_name} |

### Genres

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /top-genres              |
| POST   | /top-genres              |
| PUT    | /top-genres/{genre_name} |
| DELETE | /top-genres/{genre_name} |

### Analytics

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | /listening-summary |

## Sample Listening Summary Response

```json
{
  "total_hours": 257,
  "favorite_artist": "Future",
  "favorite_genre": "Hip-Hop",
  "total_tracks_streamed": 2385,
  "total_artist_streams": 5925
}
```

## Installation

Clone the repository:

```bash
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
cd spotify-analytics-backend
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize and seed the database:

```bash
python app/database/init_db.py
python app/database/seed_db.py
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* Search endpoints for artists, tracks, and genres
* PostgreSQL migration
* Docker support
* Authentication and authorization
* Cloud deployment
* Real Spotify API integration

## Author

Tyler Chadwick

GitHub: https://github.com/LilTeo48

LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

