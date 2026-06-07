from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_dashboard_endpoint():
    response = client.get("/analytics/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert "artist_count" in data
    assert "track_count" in data
    assert "genre_count" in data


def test_artist_search_endpoint():
    response = client.get("/search/artists?q=dr")

    assert response.status_code == 200

    data = response.json()

    assert "artists" in data
    assert isinstance(data["artists"], list)


def test_track_search_endpoint():
    response = client.get("/search/tracks?q=plan")

    assert response.status_code == 200

    data = response.json()

    assert "tracks" in data
    assert isinstance(data["tracks"], list)


def test_genre_search_endpoint():
    response = client.get("/search/genres?q=hip")

    assert response.status_code == 200

    data = response.json()

    assert "genres" in data
    assert isinstance(data["genres"], list)