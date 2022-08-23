


the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricotes']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
    print(f"A fruit count {number}")

for fruit in fruits:
    print(f"Fruit Type: {fruit}")

for i in change:
    print(f"I got {i}")


elements = []

for i in range(0,7):
    print(f"Adding {i} to the list.")
    elements.append(i)

print(elements)

for i in elements:
    print(f"Element was: {i}")