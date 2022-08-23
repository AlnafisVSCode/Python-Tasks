from xmlrpc.client import boolean


people = 30
cars = 20
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should NOT take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we need some trucks")
else:
    print("We still can't decide")

if cars > people or trucks < cars:
    print(cars > people or trucks < cars)
