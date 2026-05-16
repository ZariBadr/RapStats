import lyricsgenius

# Initialize Genius API
GENIUS_API_KEY = "vgaC3VxDr9BIOEfYDxlTtiBiJxIvZKQYDb4tln0QrRKg8DzyFBkFQdVaQ5MYrnp8"
genius = lyricsgenius.Genius(GENIUS_API_KEY)

def fetch_lyrics(artists, max_songs=None):
    """Fetches lyrics for all songs of given artists and saves them in separate files."""
    for artist_name in artists:
        print(f"Fetching songs for {artist_name}...")
        artist = genius.search_artist(artist_name, max_songs=max_songs, sort="title")
        if artist:
            output_file = f"{artist_name.replace(' ', '_')}_Lyrics.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for song in artist.songs:
                    f.write(f"\n\n=== {song.title} by {artist_name} ===\n\n")
                    f.write(song.lyrics)
                    f.write("\n" + "-" * 80 + "\n")
        else:
            print(f"Could not fetch songs for {artist_name}")

# List of chosen artists
artists_list = ["Kira7"]

# Call function to fetch lyrics and save to individual files
fetch_lyrics(artists_list)

