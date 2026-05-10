from .settings import settings
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def main():
    auth_manager = SpotifyOAuth(
        client_id=settings.spotify_client_id,
        client_secret=settings.spotify_client_secret,
        redirect_uri=settings.spotify_redirect_uri,
        scope="ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private",
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Fetch all liked songs (saved tracks) from the user's library
    saved_track_ids = set()
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        for item in results["items"]:
            saved_track_ids.add(item["track"]["id"])
        if results["next"]:
            results = sp.next(results)
        else:
            break

    logging.info(f"Found {len(saved_track_ids)} liked songs in library")

    playlists = sp.current_user_playlists()
    for playlist in playlists["items"]:
        # Only process playlists created by the current user, and skip some specific playlists by name
        if (
            playlist["owner"]["id"] == settings.spotify_user_id
            and playlist["name"] not in settings.exclude_playlists
        ):
            logging.info(f"Playlist: {playlist['name']} (ID: {playlist['id']})")

    # Check playlist songs and print those not in the user's library
    for playlist in playlists["items"]:
        if (
            playlist["owner"]["id"] == settings.spotify_user_id
            and playlist["name"] not in settings.exclude_playlists
        ):
            logging.info(
                f"Processing playlist: {playlist['name']} (ID: {playlist['id']})"
            )
            tracks = sp.playlist_tracks(playlist["id"])
            for track in tracks["items"]:
                track_id = track["item"]["id"]
                track_name = track["item"]["name"]
                # Add the songs that are not in the user's library to the library of the user
                if track_id not in saved_track_ids:
                    logging.info(
                        f"Adding track '{track_name}' (ID: {track_id}) to library"
                    )
                    sp.current_user_saved_tracks_add([track_id])


if __name__ == "__main__":
    main()
