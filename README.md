# Spotify Analytics Backend

A FastAPI backend project that simulates Spotify streaming analytics through REST API endpoints.

## Features

- Built REST APIs using FastAPI
- Returns structured JSON analytics data
- Interactive Swagger/OpenAPI documentation
- Simulated Spotify listening analytics
- Backend-focused Python application

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Backend status check |
| `/top-artists` | Returns top streamed artists |
| `/top-tracks` | Returns top streamed tracks |
| `/top-genres` | Returns most listened genres |
| `/listening-summary` | Returns overall listening statistics |

## Technologies Used

- Python
- FastAPI
- Uvicorn

## Running the Project

Install dependencies:

```bash
pip3 install fastapi uvicorn
```

Start the server:

```bash
uvicorn main:app --reload
```

Open Swagger docs:

```bash
http://127.0.0.1:8000/docs
```

## Example Response

```json
{
  "total_hours": 257,
  "favorite_artist": "Drake",
  "favorite_genre": "Hip-Hop",
  "total_tracks_streamed": 1240
}
```

## Future Improvements

- PostgreSQL database integration
- Real Spotify API integration
- Docker containerization
- User authentication
- Deployment to Render or Railway