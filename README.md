# Spotify Analytics Backend

A FastAPI backend project that simulates Spotify streaming analytics through REST API endpoints. The application provides artist, track, genre, and listening summary analytics while demonstrating RESTful API design, CRUD operations, and backend architecture best practices.

## Features

* Built with FastAPI
* RESTful API architecture
* Interactive Swagger/OpenAPI documentation
* Artist CRUD operations
* Spotify-inspired analytics endpoints
* Pydantic data validation
* Service-layer architecture
* Modular project structure
* JSON API responses

## Tech Stack

* Python
* FastAPI
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
```

## API Endpoints

### Artists

| Method | Endpoint                     | Description          |
| ------ | ---------------------------- | -------------------- |
| GET    | `/top-artists`               | Retrieve top artists |
| POST   | `/top-artists`               | Add a new artist     |
| PUT    | `/top-artists/{artist_name}` | Update an artist     |
| DELETE | `/top-artists/{artist_name}` | Delete an artist     |

### Analytics

| Method | Endpoint             | Description                   |
| ------ | -------------------- | ----------------------------- |
| GET    | `/top-tracks`        | Retrieve top streamed tracks  |
| GET    | `/top-genres`        | Retrieve top genres           |
| GET    | `/listening-summary` | Retrieve listening statistics |

## Running Locally

1. Clone the repository

```bash
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
```

2. Navigate into the project

```bash
cd spotify-analytics-backend
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the API

```bash
uvicorn app.main:app --reload
```

5. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## Sample Response

### GET /top-artists

```json
{
  "top_artists": [
    {
      "artist": "Drake",
      "streams": 9500000
    },
    {
      "artist": "The Weeknd",
      "streams": 8700000
    }
  ]
}
```

## Future Enhancements

* SQLite database integration
* PostgreSQL support
* SQLAlchemy ORM
* Docker containerization
* Authentication and authorization
* Unit and integration testing
* Real Spotify API integration

## Author

Tyler Chadwick

GitHub: https://github.com/LilTeo48

