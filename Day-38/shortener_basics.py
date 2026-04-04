import pyshorteners

url = "https://github.com/SohamPatil/50-Days-of-Python-Challenge"
s = pyshorteners.Shortener()

# Using the TinyURL engine (no API key required for basic use)
short_url = s.tinyurl.short(url)
print(f"Original: {url}")
print(f"Shortened: {short_url}")