import requests
from bs4 import BeautifulSoup

class Restaurant(object):
    name = ""
    url = ""
    dishes = []
    is_valid = False
    
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        pass
    
    def fetch_data(self):
        pass

    def fetch_soup(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def validate(self):
        pass
