class Song:
    count = 0  # Class attribute to keep track of the number of songs
    genres = []  # List to keep track of unique genres
    artists = []  # List to keep track of unique artists
    genre_count = {}  # Dictionary to keep count of each genre
    artist_count = {}  # Dictionary to keep count of each artist
    
    def __init__(self, name, artist, genre):
        self.name = name     #instance attributes
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    pass
