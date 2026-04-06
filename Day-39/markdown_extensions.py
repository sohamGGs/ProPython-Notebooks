import markdown

# Markdown with a table and a code block
md_content = """
### Project Status
| Task | Progress |
| :--- | :--- |
| Python | 80% |
| Java | 20% |

"""
html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

print("--- Advanced HTML ---")
print(html)