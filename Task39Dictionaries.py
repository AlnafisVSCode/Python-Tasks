# stuff = {'name': 'zed', 'age': 39, 'height': 6 *12 +2 }
# print(stuff['height'])


states = {
    'oragon': 'OR',
    'Florida': 'FL',
    'Cali': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


cities = {
    "CA" : "San Francisco",
    "MI" : "Detroit",
    "FL" : "JackSon"
}

#more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#PRINT THE CITIES

print("-"*30)
print("NY State has: ", cities['NY'])
print("An other city in the region is: ", cities["OR"])

print("-"*30)
print("Michigan's abbrv is: ", states["Michigan"])