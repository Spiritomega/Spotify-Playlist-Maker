import base64

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year_info = input("Which year do you want to travel to, type in YYYY-MM-DD: ")
# year_info = "2000-08-12"
url = f"https://www.billboard.com/charts/hot-100/{year_info}"

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")
top_one = soup.find(href="#",class_="c-title__link lrv-a-unstyle-link")
top_song_name = top_one.getText().strip()

songs = soup.find_all(name="h3", id="title-of-a-story",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(songs)
song_names = [song.getText().strip() for song in songs]
song_names.insert(0,top_song_name)


CLIENT_ID = "3d65fd46ff6c402f87018fe1552efc98"
CLIENT_SECRET = "16646845424e41cc8b7b90ac2ef6cd69"
REDIRECT_URL = "http://example.com"
scope = "playlist-modify-private"
username = "31skciksjdqwgnrvinrry6gtqfre"
path = "token.txt"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URL,show_dialog=True, scope=scope, username=username, cache_path=path))

user_id = sp.current_user()["id"]
print(user_id)
date = year_info.split("-")[0]
song_uri = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{date}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist")

print(song_uri)

playlist = sp.user_playlist_create(user=user_id, name=f"{date}s Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items = song_uri)







