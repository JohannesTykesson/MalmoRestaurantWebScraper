from Restaurant import Restaurant
from bs4 import BeautifulSoup
from datetime import date, datetime

class Spill(Restaurant):

    def __init__(self):
        super().__init__("Spill", "https://restaurangspill.se/")
        self.dishes = []

    def __str__(self):
        return "dishes"
    
    def fetch_data(self):
        try:
            soup = super().fetch_soup()
            elements = soup.find_all("div", class_="space-y-4")
            elements_sorted=[]
            for element in elements:
                if "Vegetarisk" in element.text:
                    elements_sorted.append(element.text)
            lunch=elements_sorted[-1].split("\n")[0]
            self.dishes=lunch.split("Vegetarisk:")
        except:
            self.is_valid = False

    def validate(self):
        try:
            soup = super().fetch_soup()
            day_today = self.days[date.today().weekday()]
            elements = soup.find_all("div", class_="space-y-4")
            for element in elements:
                if day_today in element.text:
                    self.is_valid = True
        except:
            self.is_valid = False