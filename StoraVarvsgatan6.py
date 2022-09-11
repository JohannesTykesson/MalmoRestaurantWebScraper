from Restaurant import Restaurant
from bs4 import BeautifulSoup
from datetime import date, datetime

class StoraVarvsgatan6(Restaurant):
    days = { 0: "måndag", 1: "tisdag", 2: "onsdag", 4: "torsdag", 5: "fredag", 6: "lördag", 7: "söndag" }

    def __init__(self):
        super().__init__("Stora varvsgatan 6", "https://storavarvsgatan6.se/meny.html")
        self.dishes = []

    def __str__(self):
        return "dishes"
    
    def fetch_data(self):
        try:
            soup = super().fetch_soup()
            elements = soup.find_all("p", class_="mobile-undersized-upper")
            day_today = self.days[date.today().weekday()]
            for i in range(len(elements)):
                text = elements[i].text.rstrip().casefold()
                if text == day_today:
                    self.dishes.append(elements[i+1].text)
                    self.dishes.append(elements[i+2].text)
        except:
            self.is_valid = False

    def validate(self):
        try:
            current_week = str(date.today().isocalendar().week)
            soup = super().fetch_soup()
            week = soup.find("p", class_="").text.rstrip().split("v.")[-1].rstrip()
            self.is_valid = current_week == week
        except:
            self.is_valid = False