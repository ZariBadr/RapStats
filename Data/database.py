from pymongo import MongoClient
from datetime import datetime
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def save_lyrics(artist, song_title, lyrics, source="Genius"):
    """Store scraped lyrics in MongoDB"""
    data = {
        "artist_name": artist,
        "song_title": song_title,
        "lyrics": lyrics,
        "source": source,
        "scraped_at": datetime.now()
    }
    collection.insert_one(data)
    print(f"✅ Saved: {song_title} by {artist}")

def get_lyrics(artist):
    """Retrieve lyrics from MongoDB"""
    results = collection.find({"artist_name": artist})
    for song in results:
        print(f"\n🎵 {song['song_title']} - {artist}\n{song['lyrics'][:500]}...\n{'-'*40}")

