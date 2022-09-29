from StoraVarvsgatan6 import StoraVarvsgatan6
from Spill import Spill
from MiaMarias import MiaMarias
from Saltimporten import Saltimporten

restaurants=[StoraVarvsgatan6(), Spill(), MiaMarias(), Saltimporten()]
for restaurant in restaurants:
    restaurant.fetch_data()
    print(restaurant.name)
    if restaurant.is_valid:
        restaurant.validate()
    print("Valid: " + str(restaurant.is_valid))
    print(restaurant.dishes)
    print()