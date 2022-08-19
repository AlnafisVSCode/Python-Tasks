
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count}, cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a perty!")
    print("\nget a blanket.\n")

print("We can just give the function numbers directly!:")
cheese_and_crackers(20,30)

print("Or, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6 )

print("And we can combine the two, varibles and math:")
cheese_and_crackers(amount_of_cheese+ 100, amount_of_crackers+ 1000)

#Solo Run

#Run a function with a variables Only

def birthday_cakes(sugar, salt):
    print(f"You will be needing atleast {sugar} sugar cubes for this cake.")
    print(f"And {salt} salt takes twin!")
    print("Get a blanket \n")

print("Talk about Cakes!")
# ingredients= (95, 1500)
salty = 95
sugar = 1500
birthday_cakes(salty, sugar)
#Print with some calculations done as well
print(f"adding the variable and math for salt = {salty * 1000}, and for sugar is {sugar * 10000}")
print("\nDone!\n")

print("Lastly there is the direct argument:")
print("This is going be biggggggg\n")
birthday_cakes(100000000000, 99999999999)

print("User!, What is your 1st Input?")
user_input1 = input("Salt = ")
print("User!, What is your 2nd Input?")
user_input2 = input("Sugar = ")

print(f"User: {user_input1}")
print(f"Hello User!, What is your 2nd Input?\nUser: {user_input2}\n")


birthday_cakes(user_input1,user_input2)

#s1
# print("--------------------------------------------------------------------------------------------")

# def fruits(orange, banana):
#     print(f"I can eat {banana} bananas in a day")
#     print(f"I also Lovee {orange} oranges leftovers from the x tree.\nEnd")
#     return banana

# # fruits(5, 20)                 #METHOD1

# # oranges = 10                  #METHOD 2
# # bananas = 20
# # var_fruits = fruits(oranges, bananas)
# # print(f"There is about {var_fruits} oranges left for the Guests xo, and about oranges =", var_fruits)

# # fruits(5+10, 20+20) # Calculation #Method 3

# var_Orange = 15000.10
# var_Bananas = 20000.20

# fruits(var_Orange+20, var_Bananas+20.20) #METHOD 4