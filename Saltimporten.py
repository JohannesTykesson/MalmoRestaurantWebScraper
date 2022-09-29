from Restaurant import Restaurant
from bs4 import BeautifulSoup
from datetime import date, datetime

class Saltimporten(Restaurant):

    def __init__(self):
        super().__init__("Saltimporten", "https://www.saltimporten.com/")
        self.dishes = []

    def __str__(self):
        return "dishes"
    
    def fetch_data(self):
        try:
            soup = super().fetch_soup()
            elements = soup.find_all("div", class_="meal")
            dishes_week = []
            for element in elements:
                dishes_week.append(element.text)
            self.dishes = [ dishes_week[date.today().weekday()] ]
            self.is_valid=True
        except:
            self.is_valid = False

    def validate(self):
        try:
            soup = super().fetch_soup()
            elements = soup.find_all("div", class_="date")
            dates=[]
            for element in elements:
                dates.append(element.text)
            date_today = dates[date.today().weekday()].rstrip()
            # Special case for 28/9 etc
            if len(date_today) == 4:
                date_today = date_today[:3] + '0' + date_today[3:]

            if date_today == date.today().strftime("%d/%m"):
                self.is_valid = True
            else:
                self.is_valid = False
        except:
            self.is_valid = False