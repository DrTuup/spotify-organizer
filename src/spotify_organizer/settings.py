from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings for Spotify Organizer."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    spotify_client_id: str = ""
    spotify_client_secret: str = ""
    spotify_redirect_uri: str = "http://127.0.0.1:8080/callback"
    spotify_user_id: str = ""
    spotify_cache_path: str = ".spotify_cache"

    exclude_playlists: list[str] = ["Feestje", "Mijn Shazam-nummers"]
    interval: int = 3600  # Interval in seconds between runs (default: 1 hour)


settings = Settings()
