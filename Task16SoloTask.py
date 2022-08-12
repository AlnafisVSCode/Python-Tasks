from asyncore import write
from sys import argv


script, filename = argv

print(f"Your FileName is: {filename}")

openfile = open(filename, "w")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

openfile.write(line1)
openfile.write("\n")

openfile.write(line2)
openfile.write("\n")

openfile.write(line3)
openfile.write("\n")

print("Line One Has Been Inserted!", line1)
print("Line Two Has Been Inserted!", line2)
print("Line Three Has Been Inserted!", line3)

openfile.close()