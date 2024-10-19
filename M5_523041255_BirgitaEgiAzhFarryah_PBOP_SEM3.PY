songs = [
{"title": "Love song", "artist": "Grrrl Gang", "genre": "Poppunk-Song"},
{"title": "Dewi", "artist": "Threesixty", "genre": "Poppunk-Song"},
{"title": "Hilang Harapan", "artist": "SHA", "genre": "Poppunk-Song"},
{"title": "Tipu Daya Sejarah", "artist": "The Jansen", "genre": "Poppunk-Song"},
{"title": "Kuning", "artist": "Rumah Sakit", "genre": "Poppunk-Song"},
{"title": "Kenangan Terindah", "artist": "Samsons", "genre": "Pop-Song"},
{"title": "Menghapus Jejakmu", "artist": "Peterpan", "genre": "Pop-Song"},
{"title": "Manusia Bodoh", "artist": "Ada Band", "genre": "Pop-Song"},
{"title": "11 Januari", "artist": "Gigi", "genre": "Pop-Song"},
{"title": "Semua Tentang Kita", "artist": "Peterpan", "genre": "Pop-Song"},
{"title": "Dan", "artist": "Sheila On 7", "genre": "Klasik-Song"},
{"title": "Kangen", "artist": "Dewa 19", "genre": "Klasik-Song"},
{"title": "Sempurna", "artist": "Andra", "genre": "Klasik-Song"},
{"title": "Kita", "artist": "Sheila On 7", "genre": "Klasik-Song"},
{"title": "Lama-lama", "artist": "Bernadya", "genre": "Klasik-Song"},
]

def display_all():
    print(">> List Song")
    print(f"Total Songs = {len(songs)}\n")
    print(f"{'Judul':<21}{'Penyanyi':<17}{'Genre'}")
    print("-" * 60)
    for song in songs:
        print(f"{song['title']:<21}{song['artist']:<17}{song['genre']}")
   
def display_by_genre(genre):
    print(f">> List {genre} Song")
    filtered_songs = [song for song in songs if song['genre'] == genre]
    print(f"{'Judul':<21}{'Penyanyi':<17}{'Genre'}")
    print("-" * 60)
    for song in filtered_songs:
        print(f"{song['title']:<21}{song['artist']:<17}{song['genre']}")

def search_song():
    artist = input("Masukan Penyanyi yg Ingin Di Cari: ")
    found_songs = [song for song in songs if song['artist'].lower() == artist.lower()]
    if found_songs:
        print(f"{'Judul':<21}{'Penyanyi':<17}{'Genre'}")
        print("-" * 60)
        for song in found_songs:
            print(f"{song['title']:<21}{song['artist']:<17}{song['genre']}")
    else:
        print("Penyanyi tidak ditemukan!")

def delete_song():
    display_all()
    song_title = input("\nMasukan Judul Lagu yang Ingin Dihapus: ")
    
    found_song = None
    for song in songs:
        if song['title'].lower() == song_title.lower():
            found_song = song
            break
    if found_song:
        songs.remove(found_song)
        print(f"Lagu '{found_song['title']}' telah dihapus.")
    else:
        print(f"Lagu dengan judul '{song_title}' tidak ditemukan.")


def main_menu():
    while True:
        print("\n=============================================== Playlist Music ===============================================")
        print("pilih menu : ")
        print("1. poppunk Song ==>")
        print("2. pop Song ==>")
        print("3. klasik Song ==>")
        print("4. display All ==>")
        print("5. search Music ==>")
        print("6. delete song ==>")
        print("0. Keluar")
        choice = input("Masukan Pilihan Menu : ")

        if choice == '1':
            display_by_genre("Poppunk-Song")
        elif choice == '2':
            display_by_genre("Pop-Song")
        elif choice == '3':
            display_by_genre("Klasik-Song")
        elif choice == '4':
            display_all()
        elif choice == '5':
            search_song()
        elif choice == '6':
            delete_song()
        elif choice == '0':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()