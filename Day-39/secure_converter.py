import markdown
import bleach

# Malicious Markdown attempting a Javascript injection
malicious_md = "Check this [out](javascript:alert('Hacked!'))"

# Convert to HTML
raw_html = markdown.markdown(malicious_md)

# Use bleach to strip away dangerous tags and attributes
safe_html = bleach.clean(raw_html)

print(f"Raw HTML (Dangerous): {raw_html}")
print(f"Cleaned HTML (Safe): {safe_html}")