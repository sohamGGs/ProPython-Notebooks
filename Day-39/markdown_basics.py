import markdown

md_text = "# Hello World\nThis is **bold** and this is *italic*."
html = markdown.markdown(md_text)

print("--- Generated HTML ---")
print(html)