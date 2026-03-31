from bs4 import BeautifulSoup

html_doc = """
<html><head><title>My Blog</title></head>
<body>
<p class="title"><b>The Python Journey</b></p>
<p class="content">Learning scraping is fun!</p>
<a href="http://example.com/1" id="link1">Day 1</a>
<a href="http://example.com/2" id="link2">Day 2</a>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(f"Title Tag: {soup.title.string}")
print(f"First Link: {soup.a['href']}")