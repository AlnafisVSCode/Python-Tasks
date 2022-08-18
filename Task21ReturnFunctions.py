
def add(a,b):
    print(f"Adding {a} + {b}")    
    return a + b 



print("Let's do some math with just functions!")


def substract(a, b):
    print(f"Substracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(F"Dividing {a} / {b}")
    return a / b


age = add(30, 5)
print("Adding the ages ==", age)
height = substract(10, 5)
print("Sub the height ==", height)
weight = multiply(100, 2)
iq= divide(100, 2)
print("> ", iq)

print(f"Age: {age}, height: {height}, Weight: {weight}, IQ: {iq}")

#Puzzle
print("Here is a puzzle!")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
print("-"*30)

#Solooo------------
def adding(arg1, arg2):
    print(F"Adding {arg1} and {arg2} =: {arg1+arg2}")  
x = 50
y = 50

adding(x, y)
#Moree
print("-"*30)

def litres(arg1, arg2):
    print(f"Persi owns {arg1}, and Coke owns {arg2}")
    print("Total weight in KG is: ", arg1+arg2 )
    return arg2 + arg1

pepsi = 100
coke = 200

litres(pepsi, coke)

print("So i want to see if it repeats if i use the return for same answer")
# print(litres())
alt_litres = litres(100, 500)
print(alt_litres)
