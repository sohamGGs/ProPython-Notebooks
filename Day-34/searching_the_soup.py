from bs4 import BeautifulSoup

# Finding all elements of a certain type or class
soup = BeautifulSoup(html_doc, 'html.parser')

# Find by class
title_p = soup.find("p", class_="title")
print(f"Title Paragraph: {title_p.text}")

# Find all links
all_links = soup.find_all("a")
for link in all_links:
    print(f"Link Text: {link.text} | URL: {link['href']}")