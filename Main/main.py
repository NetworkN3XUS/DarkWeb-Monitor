import requests

session = requests.Session()
session.proxies = {
    'http':  'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

response = session.get('http://check.torproject.org')
print(response.text)
