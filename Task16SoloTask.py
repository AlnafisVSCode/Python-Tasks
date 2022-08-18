from asyncore import write
from sys import argv


# script, filename = argv

# print(f"Your FileName is: {filename}")

# openfile = open(filename, "w")

# line1 = input("Line 1: ")
# line2 = input("Line 2: ")
# line3 = input("Line 3: ")

# openfile.write(line1)
# openfile.write("\n")

# openfile.write(line2)
# openfile.write("\n")

# openfile.write(line3)
# openfile.write("\n")

# print("Line One Has Been Inserted!", line1)
# print("Line Two Has Been Inserted!", line2)
# print("Line Three Has Been Inserted!", line3)

# openfile.close()

#s1
# print("-----------------------------------------------------")
script, fileName = argv

print("Script: ", script)
print(f"FileName is: {fileName}")

open_file = open(fileName, "w")


line1 = input("Line One > ")
line2 = input("Line Two > ")
line3 = input("Line Three > ")

open_file.write(f"{line1}, \n{line2}, \n{line3}")

# write_file(f"{line1}, \n{line2}, \n{line3}")

print("Line 1 Has Been Inserted!")
print("Line 2 Has Been Inserted!")
print("Line 3 Has Been Inserted!")

open_file.close()


