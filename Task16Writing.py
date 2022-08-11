from sys import argv


script, filename = argv

print(f"We're going to erase {filename}.")
print("if you don't want that, hit control-c (^c).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
targer = open(filename, 'w')

print("Truncating the file. Gooooooooodbye")
target.tra

