from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_lyrics(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Wait for JavaScript to load the lyrics
        
        # Use XPath to find the lyrics container
        lyrics_divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'Lyrics__Container') or contains(@class, 'lyrics')]")
        
        if not lyrics_divs:
            print("Could not find lyrics on the page.")
            return None

        # Extract text from all found divs
        lyrics = "\n".join([div.text for div in lyrics_divs])
        
        return lyrics.strip()

    finally:
        driver.quit()

# URL of the Genius lyrics page
genius_url = "https://genius.com/Kira7-rosa-lyrics"

lyrics = get_lyrics(genius_url)

if lyrics:
    print(lyrics)

