# EntityScrapeToolkit

## Overview

EntityScrapeToolkit is a powerful tool designed to scrape websites and extract relevant data points with ease. It not only fetches the content but also saves the scraped data into text files for further analysis or reference.

## Features

- Scrape content from any website.
- Extract relevant data points using predefined schemas.
- Save the scraped content into text files.
- Organize scraped files in a dedicated folder for easy access.

## Getting Started

### Setting Up the Environment

1. **Create a new Python virtual environment**:
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   - Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   Since we've transitioned to using a `requirements.txt` file, you can install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install playwright** (for SPAs or JS-heavy websites that require a browser to be opened):
   ```bash
   playwright install
   ```

5. **Set up your environment variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```text
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   ```

### Usage

To start scraping and saving content from predefined URLs, simply run:
```bash
python main.py
```

## Important Notes

- Always ensure you have the right to scrape a website and respect `robots.txt` and other guidelines set by the website owner.
- Use the tool responsibly to avoid overloading servers or getting IP-banned.
- This tool is intended for educational and research purposes. Always ensure you're adhering to ethical and legal standards.

---