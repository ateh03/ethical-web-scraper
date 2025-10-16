# Ethical (and Free!) Webscraper

A lightweight Python-based scraper built for transparency and of course, *ethical* data collection.
Originally written ad hoc to automate an eight hour manual task: removing the keyword instances of "DEI"from my university's website (an initiative I completely disagree with). This 70-line script saved hours of tedium and became a reusable tool for anyone who needs structured data extraction done the right way.

Enjoy responsibly!

## Features
* Plug-In Variables — modify selectors and URLs at the bottom of the file.
* Output — webscraper exports clean and deduplicated data to CSV or JSON (customizable).

## Setup
No setup required.
Clone the repo or download the script directly — it runs as-is on macOS, Linux, or Windows (Python 3.7+).

git clone https://github.com/ateh03/ethical-web-scraper.git
cd ethical-web-scraper
 
## Running
MAC OS INSTRUCTIONS: <br>
Open a terminal inside the directory

run  ```python3 web_scraper.py```<br>

## Configuration
At the bottom of the file, update the annotated variables:

BASE_URL = "https://example.com"
TARGET_KEYWORDS = ["example", "sample"]
OUTPUT_FILE = "output.csv"

These can be customized to match your own selector logic.

## Credits
𖦹 ☼ ⋆｡˚⋆ฺ Created by Ali Jamil - CIS Graduate, Technology Innovation Graduate, technologist, and (proud) automation enthusiast.
Feel free to modify or improve. 𖦹 ☼ ⋆｡˚⋆ฺ
