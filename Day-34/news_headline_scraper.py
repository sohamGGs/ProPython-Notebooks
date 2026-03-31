import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This selector depends on the website's structure
        headlines = soup.find_all('h2') 
        
        print(f"--- Headlines from {url} ---")
        for i, h in enumerate(headlines[:5], 1):
            print(f"{i}. {h.text.strip()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Using a Wikipedia page as a stable example
    get_headlines("https://en.wikipedia.org/wiki/Main_Page")