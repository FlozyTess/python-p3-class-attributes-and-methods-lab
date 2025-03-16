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

    @classmethod    #increase the song count
    def add_song_to_count(cls):         
        cls.count += 1          
        

    @classmethod   #adds unique genre
    def add_to_genres(cls, genre):          
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod    #adds unique artists
    def add_to_artists(cls, artist):        
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod   #Increment count if genre exists and initializes count if genre is new
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod    #Increment count if artist exists and initializes count if artist is new
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1    
    
    
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
hello = Song("Hello", "Adele", "Pop")
beyonce_song = Song("Halo", "Beyonce", "Pop")
another_rap_song = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

print(Song.count)  # Total number of songs
print(Song.artists)  # Unique artists
print(Song.genres)  # Unique genres
print(Song.genre_count)  # Number of songs per genre
print(Song.artist_count)  # Number of songs per artist
    
    
    
    
    
    
    
    
    
    
    
    
    
pass


