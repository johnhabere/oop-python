import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'https://open.spotify.com/artist/6d7TH1WmN4YI15WAygkuMR?si=e0NqsQKQRnCJlmJKlgBPVw'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="43cb3cca0cce496ca6c701c24c975978", client_secret="3b29696531a74083bbce7e4b2954ec10"))

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])