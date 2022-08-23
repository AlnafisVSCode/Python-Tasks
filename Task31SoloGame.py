#Here there is a game which is based off a horror story.
#Made by Alnafis

#Story: Village of Narshindi


print("""Hello Dear User!
>    What is your Name?""")
user = input("User: ")

print(f"Allright {user}, Today's game is quite simple - And you don't have to worry too much.")
print("Good Lick!", user)
print("-"*30)

print("")
print("Beginning.......")
print("Now you just woke up from sleep...")
print("...You look around and see you are in the 2nd floor with NOO light on")
print("")
print("What do you do?")
print("1. Look for the lights")
print("2. Try to look for the exit")

choice = input("> ")

if choice == "1":
    print("Eeesh. That's a sticky one NGL. BUT....")    
    print("You left your bed silently and is roaming around the floor")
    print("Cannot Find the Switch!")
    print("What do you do?")
    print("1. Yell")
    print("2. Go back to bed.")
    print("3. Start Banging everything")

    action = input("> ")

    if action == "1" and "3":
        print(f"Well {user}, it's a GG")
        print("Play again if you want.")
        print("Game Over!")
    
    elif action == "2":
        print("Congrats, you could survive the night still")
        print("You went to sleep for what it felt like eternity")
        print("gg")
    else:
        print("Good Choice, You decided that none what you have seen exist or matter.")
        print("gg")

elif choice == "2":
    print("I Will Keep this short.") 
    print("It is the better choice.")
    print("As you found the door:")
    print("1. You run down")
    print("2. You go up.")

    ending = input("> ")

    if ending == "1":
        print("Well done, you beat the game")
        print("Everybody is downstairs partying.")
        print(f"hey {user}, Go Party you deserved it.")
    elif ending == "2":
        print("Why............")
        print("The Ghost caught you upstairs.")
        print("Gg")
    else: 
        print("VOID")


