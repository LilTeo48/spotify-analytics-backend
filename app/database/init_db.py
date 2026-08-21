from app.database.db import Base, engine
from app.models.db_models import ArtistDB, TrackDB, GenreDB, PodcastDB

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created successfully")