def make_album(artist, album_name, n_tracks, release_date, k_rating = ""):
    if k_rating:
        album = {
            "artist": artist,
            "album name": album_name,
            "number of tracks": n_tracks,
            "release date": release_date,
            "KERANG rating": k_rating
            }
    else:
        album = {
        "artist": artist,
        "album name": album_name,
        "number of tracks": n_tracks,
        "release date": release_date,
        }
    return album