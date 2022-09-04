# stuff = {'name': 'zed', 'age': 39, 'height': 6 *12 +2 }
# print(stuff['height'])




# states = {
#     'oragon': 'OR',
#     'Florida': 'FL',
#     'Cali': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }


# cities = {
#     "CA" : "San Francisco",
#     "MI" : "Detroit",
#     "FL" : "JackSon"
# }

# #more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# #PRINT THE CITIES

# print("-"*30)
# print("NY State has: ", cities['NY'])
# print("An other city in the region is: ", cities["OR"])

# print("-"*30)
# print("Michigan's abbrv is: ", states["Michigan"])
# print("Florida's Abbvs is: ", states['Florida'] )

# #More Complicated - do it by using the state then cities dict
# print("-"*30)
# print("Michingan has: ", cities[states['Michigan']])
# print("Florida has: ", cities[states['Florida']])

# #print every state abbreviation
# print("-"*30)

# # for abbrv, city in list(cities.items()):
# #     print(f"{abbrv} has the city {city}")

# for abrv, city in list(cities.items()):
#     print(f"{abrv} has the city {city}")

# # now do both at the same time
# print("-"*30)
# for state, abbrv in list(states.items()):
#     print(f"{state} state is abbreviation for {abbrv}")
#     print(f"and has city {cities,[abbrv]}")
# print("-"*30)

# #safely get a abbreviation by state that might not be there

# state = states.get("Texas")

# if not state:
#     print("Sorry, no Texas.")

# # get a city with a default value

# city = cities.get("TX", "L Does Not Exist")
# print(f"The city for the state 'TX' is : {city}")

#s2 SOLO
print("--------------------------------------------------------")

cities = {
    "LN" : "London",
    "BR" : "Birmingham",
    "CH" : "Chelsea",
    "LP" : "Liverpool",
    "MN" : "Manchester"
}

region = {

}