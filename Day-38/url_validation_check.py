import requests
import pyshorteners

def safe_shorten(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code < 400:
            return pyshorteners.Shortener().tinyurl.short(url)
        else:
            return "Error: URL is unreachable."
    except Exception as e:
        return f"Error: {e}"

print(safe_shorten("https://google.com"))