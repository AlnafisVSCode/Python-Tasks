from ast import Eq


print("Let's practice everything!.")
print('You\'d need to know \'bout escapes with \\ that do:')# What \ Does
print("You'd need to know 'bout escapes with \ that do:")
print("newlines\nand \t tabs.")

poem = """
\tThe lovely world 
with logic so firmly planted 
cannot discent \n the needs of love 
nor comprehend passion from instuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-"*20)
print(poem)
print("-"*20)
print("")
five = 10-2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
b,j,c = secret_formula(start_point)

#An other method to do "f" == .format()
print("With a starting point of : {}".format(start_point))
#Look Down
print(f"We'd have {b} beans, {j} jars, and {c} crates") 

start_point = start_point / 10

print("We can also do that this way: ")
formula = secret_formula(start_point)
#Interesting (*...Stuff)
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
    
                                                  
