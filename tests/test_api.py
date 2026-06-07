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

def test_top_artists_endpoint():
    response = client.get("/top-artists")

    assert response.status_code == 200

    data = response.json()

    assert "top_artists" in data
    assert isinstance(data["top_artists"], list)


def test_top_tracks_endpoint():
    response = client.get("/top-tracks")

    assert response.status_code == 200

    data = response.json()

    assert "top_tracks" in data
    assert isinstance(data["top_tracks"], list)


def test_top_genres_endpoint():
    response = client.get("/top-genres")

    assert response.status_code == 200

    data = response.json()

    assert "top_genres" in data
    assert isinstance(data["top_genres"], list)


def test_top_artists_filter_sort_limit():
    response = client.get("/top-artists?min_streams=1000&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_artists" in data
    assert len(data["top_artists"]) <= 2


def test_top_tracks_filter_sort_limit():
    response = client.get("/top-tracks?artist=Future&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_tracks" in data
    assert isinstance(data["top_tracks"], list)


def test_top_genres_filter_sort_limit():
    response = client.get("/top-genres?min_hours=50&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_genres" in data
    assert len(data["top_genres"]) <= 2  

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_database_health_endpoint():
    response = client.get("/health/database")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data

def test_get_podcasts_endpoint():
    response = client.get("/podcasts")

    assert response.status_code == 200


def test_search_podcasts_endpoint():
    response = client.get("/search/podcasts?q=pard")

    assert response.status_code == 200

    data = response.json()

    assert "podcasts" in data
    assert isinstance(data["podcasts"], list)          