from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time

def get_song_links(artist_url):
    """Scrape song links from Genius artist page"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without opening browser
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(artist_url)
    
    time.sleep(3)  # Wait for page load
    
    song_links = []
    elements = driver.find_elements(By.XPATH, '//a[contains(@href, "genius.com")]')
    for element in elements:
        link = element.get_attribute("href")
        if "/lyrics" in link and link not in song_links:
            song_links.append(link)

    driver.quit()
    return song_links

def get_lyrics(song_url):
    """Extract lyrics from Genius song page"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(song_url, headers=headers)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    lyrics_div = soup.find("div", class_="Lyrics__Container")

    if lyrics_div:
        return "\n".join([p.get_text() for p in lyrics_div.find_all("p")])
    
    return None

