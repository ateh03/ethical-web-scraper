import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            continue
        urls.add(href)
    return urls

def search_for_text(url, text):
    """
    Searches for the given text in webpage content
    """
    try:
        response = requests.get(url)
        if text.lower() in response.text.lower():
            return True
    except requests.RequestException:
        return False
    return False

def scrape_website_for_text(start_url, text):
    """
    Scrape a website and report URLs containing a specific text
    """
    urls = get_all_website_links(start_url)
    pages_with_text = []
    for url in urls:
        if search_for_text(url, text):
            pages_with_text.append(url)

    return pages_with_text

# Replace 'your_url_here' with your starting URL
start_url = 'https://sc.edu/study/colleges_schools/moore/index.php'

# Replace with keyword you want to scrape for
text_to_search = "diversity and inclusion"
pages = scrape_website_for_text(start_url, text_to_search)
print(pages)
