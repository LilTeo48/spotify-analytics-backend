import os

import httpx


SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"


class SpotifyClient:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set"
            )

    def get_access_token(self) -> str:
        response = httpx.post(
            SPOTIFY_TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.client_secret),
            timeout=10.0,
        )

        response.raise_for_status()
        return response.json()["access_token"]

    def search_artist(self, artist_name: str) -> dict | None:
        access_token = self.get_access_token()

        response = httpx.get(
            f"{SPOTIFY_API_BASE_URL}/search",
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            params={
                "q": artist_name,
                "type": "artist",
                "limit": 1,
            },
            timeout=10.0,
        )

        response.raise_for_status()

        artists = response.json().get(
            "artists", {}
        ).get("items", [])

        if not artists:
            return None

        return artists[0]