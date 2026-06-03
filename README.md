# Spotify Analytics Backend

A backend analytics API built with FastAPI, SQLAlchemy, and SQLite that provides Spotify-inspired music analytics, search functionality, CRUD operations, and KPI reporting.

## Features

### Artist Management

* Create artists
* View artists
* Update artist information
* Delete artists
* Search artists by name

### Track Management

* Create tracks
* View tracks
* Update track information
* Delete tracks
* Search tracks by name

### Genre Management

* Create genres
* View genres
* Update genre information
* Delete genres
* Search genres by name

### Analytics & Reporting

* Listening summary dashboard
* Top artist analytics
* Top track analytics
* Top genre analytics
* Dashboard KPI endpoint
* Total streams analytics
* Total listening hours analytics
* Database record counts

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

## API Endpoints

### Artists

| Method | Endpoint                          |
| ------ | --------------------------------- |
| GET    | /top-artists                      |
| POST   | /top-artists                      |
| PUT    | /top-artists/{artist_name}        |
| DELETE | /top-artists/{artist_name}        |
| GET    | /top-artists/search/{artist_name} |

### Tracks

| Method | Endpoint                        |
| ------ | ------------------------------- |
| GET    | /top-tracks                     |
| POST   | /top-tracks                     |
| PUT    | /top-tracks/{track_name}        |
| DELETE | /top-tracks/{track_name}        |
| GET    | /top-tracks/search/{track_name} |

### Genres

| Method | Endpoint                        |
| ------ | ------------------------------- |
| GET    | /top-genres                     |
| POST   | /top-genres                     |
| PUT    | /top-genres/{genre_name}        |
| DELETE | /top-genres/{genre_name}        |
| GET    | /top-genres/search/{genre_name} |

### Analytics

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /listening-summary       |
| GET    | /analytics/top-artist    |
| GET    | /analytics/top-track     |
| GET    | /analytics/top-genre     |
| GET    | /analytics/dashboard     |
| GET    | /analytics/counts        |
| GET    | /analytics/total-streams |
| GET    | /analytics/total-hours   |

## Running Locally

Clone the repository:

```bash
git clone https://github.com/LilTeo48/spotify-analytics-backend.git
cd spotify-analytics-backend
```

Create and activate a virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* Filtering endpoints
* Sorting endpoints
* Pagination
* PostgreSQL support
* Docker deployment
* Authentication and authorization
* Cloud deployment

## Author

Tyler Chadwick


GitHub: https://github.com/LilTeo48

LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275

