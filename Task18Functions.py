"""
1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you ”end” your function by going back to writing with no indent (dedenting we call it)?

When you run (”use” or ”call”) a function, check these things:

1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?
Use these two checklists on the remaining lessons until you do not need them anymore.
Finally, repeat this a few times to yourself:
”To ’ run , ’ ’ c a l l , ’ or ’ use ’ a function a l l mean the same thing . ”
"""


var = 1+1
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#Much more effiecnient in creating function as it's not necessary to unpack!!
#Just unpack everything () inside like arg1, arg2 in front of def + varName --> then print
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


#Only PRINTS ONE
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin.")

    
print_two("Zed", "Been")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

print("So 1+1 is: ", var)
#Space++++++++++++++++++

#Solo

#Function with no argumanets

def print_nonee():
    print("I got Nothing2")

print_nonee()

#print 1 argument:

def print_Onee(arg1):
    print("Arg Onee iss:", arg1)


print_Onee("Shit Up")

#Prints 2 with unpacking args

def print_2(*args):
    peanut, allu = args
    print(f"My ARGS are: {peanut} and {allu}")

print_2("Peanutas", "Alloys")


#Print 2 without unpacking!

def printingTwo(arg1, arg2):
    print(f"These are 2 of unpacked arguments: {arg1} and {arg2}")
    print("That's all to it bbabyyy!!")

printingTwo("Microphone", "Oven?")


