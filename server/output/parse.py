from bs4 import BeautifulSoup
import json

def extract_element_data(tag):
    return {
        "tag": tag.name,
        "text": tag.get_text(strip=True),
        "attributes": tag.attrs,
        "html": str(tag)
    }

# Load HTML
with open("page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Tags to scrape (can expand)
target_tags = ["h1", "h2", "h3", "p", "a", "li", "strong", "button", "span", "div"]

data = []
for tag in soup.find_all(target_tags):
    text = tag.get_text(strip=True)
    if text:  # Only include if there's visible text
        element_data = extract_element_data(tag)
        data.append(element_data)

# Save to JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
