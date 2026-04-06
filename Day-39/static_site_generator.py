import markdown

# A simple HTML template with CSS styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Python Journey</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 40px auto; padding: 0 20px; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 15px; border-left: 5px solid #333; overflow-x: auto; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #eee; }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def build_page(input_md, output_html):
    # 1. Read the Markdown file
    with open(input_md, "r") as f:
        md_content = f.read()
    
    # 2. Convert content to HTML
    body_html = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    
    # 3. Inject into template
    final_html = HTML_TEMPLATE.format(content=body_html)
    
    # 4. Save the result
    with open(output_html, "w") as f:
        f.write(final_html)
    print(f"🚀 Success! '{output_html}' has been generated.")

if __name__ == "__main__":
    # Create a test Markdown file
    with open("blog_post.md", "w") as f:
        f.write("# Day 39: Automation\n\nI am building a **Static Site Generator** today!")
    
    build_page("blog_post.md", "index.html")