# # 8-6. City names.

# def city_country(city, country):
#     a = print(f"{city.title()}, {country.title()}")
#     return a

# city_country("Melbourne", "Australia")
# city_country("Berlin", "Germany")
# city_country("Tokyo", "Japan")

# 8-7. Album.

# import functions0 as func
from functions0 import make_album as func_album

albums = []

while True:
    in_artist = input("Enter name of the artist or band: ").lower()
    if in_artist == 'q':
        break
    in_album_name = input("Enter the name of the album: ")
    if in_album_name == 'q':
        break
    in_n_tracks = input("Enter number of tracks: ")
    if in_n_tracks == 'q':
        break
    in_release_date = input("Enter the release date: ")
    if in_release_date == 'q':
        break
    in_k_rating = input("Enter KERANG's rating out of 10 or hit Enter to skip: ")
    if in_k_rating == 'q':
        break

    albums.append(func_album(in_artist, in_album_name, in_n_tracks, in_release_date, in_k_rating))
    
    for i in albums:
        for j, k in i.items():
            print(f"{j.title()}: {k.title()}")

