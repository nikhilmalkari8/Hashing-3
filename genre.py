from collections import defaultdict

def favoriteGenres(users, songs, genres):
    # Step 1: Map each song to its genre
    song_to_genre = {}
    for i, song in enumerate(songs):
        song_to_genre[song] = genres[i]
    
    # Step 2: For each user, count the number of songs in each genre
    result = []
    for user in users:
        user_id, user_songs = list(user.items())[0]  # Extract user name and songs they listened to
        genre_count = defaultdict(int)
        
        for song in user_songs:
            genre = song_to_genre.get(song)
            if genre:
                genre_count[genre] += 1
        
        # Step 3: Find the genre(s) with the maximum count
        if genre_count:
            max_count = max(genre_count.values())
            favorite_genres = [genre for genre, count in genre_count.items() if count == max_count]
            favorite_genres.sort()  # Sort genres alphabetically
            result.append({user_id: favorite_genres})
    
    return result
