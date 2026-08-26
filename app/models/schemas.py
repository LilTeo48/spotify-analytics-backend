from pydantic import BaseModel


class Artist(BaseModel):
    artist: str
    streams: int


class Track(BaseModel):
    track: str
    artist: str
    streams: int


class Genre(BaseModel):
    genre: str
    hours_listened: int


class ListeningSummary(BaseModel):
    total_hours: int
    favorite_artist: str
    favorite_genre: str
    total_tracks_streamed: int


class Podcast(BaseModel):
    podcast_name: str
    host: str
    category: str
    episodes: int
    hours_listened: int


class ArtistAnalyticsItem(BaseModel):
    id: int
    artist: str
    streams: int


class TrackAnalyticsItem(BaseModel):
    id: int
    track: str
    artist: str
    streams: int


class GenreAnalyticsItem(BaseModel):
    id: int
    genre: str
    hours_listened: int


class TopArtistAnalytics(BaseModel):
    top_artist: ArtistAnalyticsItem


class TopTrackAnalytics(BaseModel):
    top_track: TrackAnalyticsItem


class TopGenreAnalytics(BaseModel):
    top_genre: GenreAnalyticsItem


class CountsAnalytics(BaseModel):
    artist_count: int
    track_count: int
    genre_count: int


class TotalStreamsAnalytics(BaseModel):
    total_artist_streams: int
    total_track_streams: int
    combined_streams: int


class TotalHoursAnalytics(BaseModel):
    total_hours_listened: int


class DashboardAnalytics(BaseModel):
    artist_count: int
    track_count: int
    genre_count: int
    total_artist_streams: int
    total_track_streams: int
    total_hours_listened: int
    top_artist: str | None
    top_track: str | None
    top_genre: str | None