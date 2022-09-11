from StoraVarvsgatan6 import StoraVarvsgatan6

r1 = StoraVarvsgatan6()
print(r1.name)

print(r1.is_valid)
r1.validate()
print(r1.is_valid)

r1.fetch_data()
print(r1.dishes)