from Restaurant import Restaurant
from bs4 import BeautifulSoup
from datetime import date, datetime

class MiaMarias(Restaurant):

    def __init__(self):
        super().__init__("MiaMarias", "http://www.miamarias.nu/")
        self.dishes = []

    def __str__(self):
        return "dishes"
    
    def fetch_data(self):
        try:
            soup = super().fetch_soup()
            elements = soup.find_all("tbody")
            lunch_today=elements[date.today().weekday()].text.split("\n")
            lunch_today_filtered=filter(lambda x: x.rstrip() != "" and "kr" not in x, lunch_today)
            for lunch in lunch_today_filtered:
                self.dishes.append(lunch)
            self.is_valid=True
        except:
            self.is_valid = False

    def validate(self):
        try:
            self.is_valid = True
        except:
            self.is_valid = False