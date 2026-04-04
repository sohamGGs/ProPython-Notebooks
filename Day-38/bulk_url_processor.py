import pyshorteners

def bulk_process(url_list):
    s = pyshorteners.Shortener()
    results = {}
    for url in url_list:
        try:
            results[url] = s.tinyurl.short(url)
        except:
            results[url] = "Failed"
    return results

if __name__ == "__main__":
    my_links = ["https://python.org", "https://stackoverflow.com"]
    mapped = bulk_process(my_links)
    for orig, short in mapped.items():
        print(f"{short} -> {orig}")