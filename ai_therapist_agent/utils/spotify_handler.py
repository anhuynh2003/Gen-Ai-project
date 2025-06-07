# utils/spotify_handler.py

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

def get_track_preview(query: str) -> str:
    results = sp.search(q=query, type="track", limit=1)
    tracks = results.get('tracks', {}).get('items', [])

    if not tracks:
        return "[No track found.]"

    track = tracks[0]
    name = track['name']
    artist = track['artists'][0]['name']
    preview_url = track.get('preview_url', 'No preview available')

    return f"🎧 **{name}** by {artist}\nPreview: {preview_url}"
