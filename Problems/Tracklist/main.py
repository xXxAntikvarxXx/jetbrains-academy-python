def tracklist(**kwargs):
    for artist, albums in kwargs.items():
        print(artist)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")
