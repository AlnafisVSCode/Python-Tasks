from sys import argv


script, filename = argv

print(f"We're going to erase {filename}.")
print("if you don't want that, hit control-c (^c).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Gooooooooodbye")
# target.trancate()

print("Now Im going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

##SOLOOO!!!!!!! So Much Efficiency
target.write(f"{line1}\n{line2}\n{line3}\n")


print("And we are finally, Closing this shhhhhhhhhhit Twinn.")
target.close()
#Now We Gon Try Our selves Creating what we did previosuly on our ownn Twin

#Also Comment out before last Comment as it's the real Example but leave this onward for us

#It's On Task16 Solo Page



