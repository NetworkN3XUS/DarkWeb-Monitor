import requests
from bs4 import BeautifulSoup

def scrape_onion_site(url):
    session = requests.Session()
    session.proxies = {
        'http':  'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Example: Scrape a .onion site (replace with actual URL)
url = 'http://exampleonionaddress.onion'
content = scrape_onion_site(url)
print(content.prettify())  # Print out the prettified HTML

