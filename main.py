import asyncio
import pprint
import os

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright

def format_output(extracted_content):
    formatted_content = ""
    for item in extracted_content:
        headline = item.get('news_headline', '')
        summary = item.get('news_short_summary', '')
        formatted_content += f"{headline}\n{summary}\n\n"
    return formatted_content

async def scrape_and_save_content(url, tags, schema_pydantic):
    html_content = await ascrape_playwright(url, tags)
    extracted_content = extract(content=html_content[:4000], schema_pydantic=schema_pydantic)
    formatted_content = format_output(extracted_content)
    
    # Extract the website's title for the filename
    title = url.split("//")[-1].split("/")[0]
    filename = f"{title}.txt"
    
    # Ensure the "scraped_content" directory exists
    if not os.path.exists("scraped_content"):
        os.makedirs("scraped_content")

    filepath = os.path.join("scraped_content", filename)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Content from {title} saved to {filepath}.")

if __name__ == "__main__":
    urls = [
        "https://www.cnn.com",
        "https://www.wsj.com",
        "https://www.nytimes.com/ca/",
        "https://www.amazon.ca/s?k=computers&crid=1LUXGQOD2ULFD&sprefix=%2Caps%2C94&ref=nb_sb_ss_recent_1_0_recent"
    ]

    for url in urls:
        asyncio.run(scrape_and_save_content(url, ["span"], SchemaNewsWebsites))