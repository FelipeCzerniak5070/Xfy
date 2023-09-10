import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = "4ed3a24f6ed141698293c114374ec0e2"
spotify_client_secret = "57f2221137084a5da63c3b66b5b9fbf9"
redirect_uri = "https://google.com"

# Configurar as credenciais do Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-read-playback-state'))

# Obter informações sobre a música atualmente em reprodução
current_track = sp.current_playback()
if current_track is not None and 'item' in current_track:
    album_name = current_track['item']['album']['name']
    track_name = current_track['item']['name']
    artist_name = current_track['item']['artists'][0]['name']
    album_cover = current_track['item']['album']['images'][0]['url']
    print(f"Você está ouvindo: {track_name} por {artist_name} no album {album_name}.")
    webbrowser.open_new_tab(album_cover)
else:
    print("Nenhuma música está sendo reproduzida no momento.")  