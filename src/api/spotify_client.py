from config.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="user-library-read playlist-modify-public"
        ))

    def get_saved_tracks(self, limit=50, offset=0):
        """Busca um lote de músicas curtidas do usuário."""
        return self.sp.current_user_saved_tracks(limit=limit, offset=offset)

    def get_artist_genres(self, artist_id):
        """Busca os gêneros do artista."""
        return self.sp.artist(artist_id).get("genres", [])

    def create_playlist(self, user_id, name, description=""):
        """Cria uma playlist no Spotify."""
        return self.sp.user_playlist_create(user_id, name, description=description)

    def add_tracks_to_playlist(self, playlist_id, track_uris):
        """Adiciona faixas a uma playlist."""
        self.sp.playlist_add_items(playlist_id, track_uris)
