# Spotify Analytics Backend

A backend analytics platform inspired by Spotify, built with FastAPI, SQLAlchemy, and PostgreSQL/SQLite.

The application provides RESTful APIs for managing artists, tracks, genres, and podcasts while exposing analytics-focused endpoints for search, rankings, listening metrics, database summaries, and health monitoring.

## Features

### Core Functionality

- Artist Management
- Track Management
- Genre Management
- Podcast Management
- RESTful CRUD Operations
- Search Endpoints
- FastAPI Swagger Documentation
- Query Parameter Validation
- 404 Error Handling for Missing Resources

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
- Search Artists, Tracks, Genres, and Podcasts
- API Health Check
- Database Health Monitoring

## Engineering Features

- FastAPI Backend Architecture
- SQLAlchemy ORM
- PostgreSQL / SQLite Support
- Pydantic Response Models
- FastAPI Query Validation
- Modular Route and Service Layer Design
- Automated Testing with Pytest
- CRUD Regression Testing
- Error-Handling Tests
- Analytics Endpoint Tests
- GitHub Actions CI/CD
- Docker and Docker Compose Support

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
- Git / GitHub

## API Endpoints

### Health

```text
GET /health
GET /health/database

## Author

**Tyler Chadwick**

GitHub:  
https://github.com/LilTeo48

LinkedIn:  
https://www.linkedin.com/in/tyler-chadwick-81b9a6275
