from fastapi import APIRouter, HTTPException, Query
import httpx

from app.integrations.spotify_client import SpotifyClient


router = APIRouter(
    prefix="/spotify",
    tags=["Spotify"],
)


@router.get("/artists/search")
def search_artist(
    name: str = Query(..., min_length=1, description="Artist name to search for")
):
    try:
        artist = SpotifyClient().search_artist(name)

        if artist is None:
            raise HTTPException(
                status_code=404,
                detail=f"Artist '{name}' not found",
            )

        return {
            "spotify_id": artist["id"],
            "name": artist["name"],
            "spotify_url": artist["external_urls"]["spotify"],
            "images": artist.get("images", []),
        }

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail="Spotify API request failed",
        ) from exc


@router.get("/tracks/search")
def search_track(
    name: str = Query(..., min_length=1, description="Track name to search for")
):
    try:
        track = SpotifyClient().search_track(name)

        if track is None:
            raise HTTPException(
                status_code=404,
                detail=f"Track '{name}' not found",
            )

        return {
            "spotify_id": track["id"],
            "name": track["name"],
            "artists": [
                artist["name"]
                for artist in track.get("artists", [])
            ],
            "album": track.get("album", {}).get("name"),
            "spotify_url": track["external_urls"]["spotify"],
            "duration_ms": track.get("duration_ms"),
        }

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail="Spotify API request failed",
        ) from exc