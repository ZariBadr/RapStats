from scraper import get_song_links, get_lyrics
from database import save_lyrics

def scrape_genius_artist(artist_name):
    """Main function to scrape and store lyrics for an artist"""
    artist_url = f"https://genius.com/artists/{artist_name.replace(' ', '')}"
    
    print(f"🎤 Scraping songs for: {artist_name}...")
    song_links = get_song_links(artist_url)

    for song_url in song_links:
        song_title = song_url.split("/")[-1].replace("-", " ").replace("lyrics", "").strip()
        lyrics = get_lyrics(song_url)
        
        if lyrics:
            save_lyrics(artist_name, song_title, lyrics, "Genius")
        else:
            print(f"❌ Failed to fetch lyrics for {song_title}")

if __name__ == "__main__":
    # Add the artists you want to scrape
    artists = ["ElGrandeToto", "Tagne", "Draganov", "Stormy", "Madd"]
    
    for artist in artists:
        scrape_genius_artist(artist)

