from collections import Counter
import string

def analyze_lyrics(file_path, artist_name):
    """Analyzes lyrics to determine unique word count, total word count, and top 3 most used words (above 4 letters)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = text.split()

            total_word_count = len(words)
            unique_word_count = len(set(words))

            # Filter words to include only those with more than 4 letters
            filtered_words = [word for word in words if len(word) > 4]
            word_counts = Counter(filtered_words)
            top_3_words = word_counts.most_common(3)

            # Formatting results
            top_words_str = " - ".join([word for word, count in top_3_words]) if top_3_words else "N/A"
            result = (
                f"Name of artist: {artist_name}\n"
                f"- Total unique words per total words: {unique_word_count} / {total_word_count}\n"
                f"- Top 3 most used words (more than 4 letters): {top_words_str}\n\n"
            )

            # Save results to file
            with open("everyArtistData.txt", "a", encoding="utf-8") as output_file:
                output_file.write(result)
            
            print("Analysis completed and saved to 'everyArtistData.txt'.")
    
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "Kira7_Lyrics.txt"  # Replace with your file path
artist_name = "Kira7"  # Replace with the artist's name
analyze_lyrics(file_path, artist_name)

