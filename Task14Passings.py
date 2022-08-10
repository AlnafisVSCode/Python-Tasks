from sys import argv
# WHAT I HAVE DO TO MAKE IT WITHOUT STATING IT'S A SCRIPT AND RUNNING W MY NAME AS GAME 
# print("Your Name?")
# user_name = input()
# prompt = '> '

# # print(f"hi {user_name}, #I'm the {scriptss}, script.")
# print(f"hi {user_name}, I'm the script.")
# print("I'd live to ask you a few questions.")
# print(f"Do you like {user_name}?")
# likes = input(prompt)
# print(f"Very cool, i also like {user_name}.")
# #Space
# print("")
# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input("> ")

# print(f"""
# > Allright, so you said {likes} about liking me. 
# You live in {lives}. Not sure where that is though.
# And you have a {computer} computer. Nice Brudda.
# """)
# #Space
# print("*" * 30)
# print("")
#-----------------------------------------------------------------------------------------
print("Your Name?")
script, user_name = argv
prompt = '> '

print(f"hi {user_name}, #I'm the {script}, script.")
# print(f"hi {user_name}, I'm the script.")
print("I'd live to ask you a few questions.")
print(f"Do you like {user_name}?")
likes = input(prompt)
print(f"Very cool, i also like {user_name}.")
#Space
print("")
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input("> ")

print(f"""
> Allright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is though.
And you have a {computer} computer. Nice Brudda.
""")
#Space
print("*" * 30)
print("")







