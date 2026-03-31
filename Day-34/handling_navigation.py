from bs4 import BeautifulSoup

html = "<div><ul id='list'><li>Item 1</li><li>Item 2</li></ul></div>"
soup = BeautifulSoup(html, 'html.parser')

# Navigate to the <ul> then find all <li>
u_list = soup.find(id="list")
items = [li.text for li in u_list.find_all("li")]

print(f"Extracted List: {items}")