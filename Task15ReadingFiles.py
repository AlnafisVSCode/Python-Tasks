from asyncore import read
from sys import argv

# print("What is the File Name BOY")
#Creating the arguament and it allows us to input using our script argv
filename= input()

#open() opens the file and it stores it in the var!
txt = open(filename)

print(f"Here is you file {filename}:")
print(txt.read()) #it reads the file which it then prints using the print 

#Looops
print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)
# print(txt_again.read()) It will read the whole thing

#https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
#Space - Read One Line!!
print(txt_again.readline()) 

print(txt_again.readline())
#Read all each Lines!!!!
print(txt_again.readlines())
print(txt_again.readlines())

#To Empty File;;
# txt.truncate()
txt.close()
txt_again.close()







# title = 'fllllllllllllllllllllllllpalpefpakfoakfoksofe'

# script, filename = argv
# # file_again = "ex15_sample.txt"
# txt = open(filename)
# print(f"Here is you file {filename}:")
# print(txt.read()) 

# filename.write("title")
# # print(title)

# filename.close()

# #s1
# # print("-----------------------------------------------------")

# print("What is the file name?")
# file_name = input("> ")
# open_file = open(file_name)
# print(f"Name of the file is: {file_name}")
# # print(open_file.readlines())
# print(open_file.read())


