from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings for Spotify Organizer."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    spotify_client_id: str = ""
    spotify_client_secret: str = ""
    spotify_redirect_uri: str = "http://127.0.0.1:8080/callback"
    spotify_user_id: str = ""

    exclude_playlists: list[str] = ["Feestje", "Mijn Shazam-nummers"]


settings = Settings()
