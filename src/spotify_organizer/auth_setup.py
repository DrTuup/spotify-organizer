from spotify_organizer.settings import settings
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Run this locally to generate .spotify_cache
auth_manager = SpotifyOAuth(
    client_id=settings.spotify_client_id,
    client_secret=settings.spotify_client_secret,
    redirect_uri=settings.spotify_redirect_uri,
    scope="ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private",
    cache_path=".spotify_cache",
)
sp = spotipy.Spotify(auth_manager=auth_manager)
print("Authenticated as:", sp.current_user()["display_name"])
print("Cache saved to .spotify_cache")
