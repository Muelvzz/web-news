import requests


def extract_news(get_url):
    response = requests.get(get_url)
    content = response.json()
    return content
