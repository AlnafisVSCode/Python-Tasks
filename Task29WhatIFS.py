people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats!, baraboom!")

if people > cats:
    print("Not many cats, actually saved lol")

if people < dogs:
    print("The words is drooolin")

if people > dogs:
    print("The words is dryyyyyyyy")

dogs += 5
#dogs = dogs + 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs, daymm bigg dawgh")

if cats >= dogs or (not(people == dogs or people > cats)):
    print(cats >= dogs or (not(people == dogs or people > cats)))


