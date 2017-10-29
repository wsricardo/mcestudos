import spotipy

sp = spotipy.Spotify()
uri = 'spotify:artist:4gzpq5DPGxSnKTe4SA8HAU'
results = sp.artist_top_tracks(uri)

for track in results['tracks'][:10]:
    print ('Track    : ' + track['name'])
    if track['preview_url']:
        print ('Audio    : ' + track['preview_url'])
    print ('Cover art: ' + track['album']['images'][0]['url'])
    print ('Url album: ' + track['album']['external_urls']['spotify'])
    print ()
print ()
print ('Albums')
results = sp.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
