#gold room
#Trap Door
#snake_room
#Dead
#Start



userA = input("Hello User, What is your name ?")
user = userA+":" 


def start():
    # print("Hello User, What is your name ?", end= "")
    # user = input()
    print(user, "you are in a cave!\nYou Have 2 Choices 'Left' or 'Right'")

    choice = input(f"{user} ")

    if "right" in choice:
        print("Interesting...\nYou Entered the snake room....")
        snake_room()

    elif "left" in choice:
        print("Okay...\nBe Alert it's a trap door!!")
        trap_door()
    
    else:
        print("Why Didn't you choose what we asked you....\n....")
        dead()


def dead():
    print("You are currently in the dead Room...\nNot A Joke...")
    print("Waiting Room...")
    print("""    :----------------------Dead--------------------------------:
    :-----------------------Dead-------------------------------:
    :------------------------Dead------------------------------:
    :-------------------------Dead-----------------------------:
    :--------------------------Dead----------------------------:
    :---------------------------Dead---------------------------:
    :----------------------------Dead--------------------------:
    :-----------------------Dead-------------------------------:
    :------------------------Dead------------------------------:
    :-------------------------Dead-----------------------------:
    :--------------------------Dead----------------------------:
    :---------------------------Dead---------------------------:
    :----------------------------Dead--------------------------:
    :-----------------------Dead-------------------------------:
    :------------------------Dead------------------------------:
    :-------------------------Dead-----------------------------:
    :--------------------------Dead----------------------------:
    :---------------------------Dead---------------------------:
    :----------------------------GameOver----------------------:""")
    exit(0)

def trap_door():
    print("\tWelcome to the Trap Door!!\n There is 2 Doors: 'red' and 'blue'\nWhich one you choose?")
    print("\tp.s: Blue Could be easier...")

    choice = input(user)

    if "red" in choice:
        print("I don't mind Red but...\nITS A REDD WORLD!!!!!!")
        print("Go Back where you came from and choose 'Blue'!")
        start()
    
    elif "blue" in choice:
        print("Sikeee\nBlue Aint either.")    
        print("What do you do?")
        trap_door()
    else:
        print("Congrats......")
        last_trap()

def last_trap():
    print("You have your last chance to win Big\n50/50 Chance>>> '1' or '2'")

    choice = input(user)

    if "1" in choice or "2" in choice:
        numberz = int(choice)

    else:
        print("Print a Damn Number Dumass")
        last_trap()

    if "1" in numberz:
        print("If you aint first\nYou Last...")
        gold_room()
    elif "2" in numberz:
        print("Well I did say 50% Chance of getting this.\nCyu.....")
        dead()
    else:
        print("Choose Wisely!")
        last_trap()

def snake_room():
    print("")
    print(f"Welcome To the Snake Room {user}!!!!\n The golden ticket is right in front of you.")
    print("1.'Run' for it?\n2.'Hit' the snakes?\n3.'Use the 'Torch' to scare the snakes?\n4. 'Open' door?")

    snake_moved = False

    while True:
        choice = input(user)

        if choice == "run":
            print("What is Wrong with you???")
            dead()

        elif choice == "hit":
            print("Some of them are venomus\nNow you have 1/2 Health!")
            
        elif choice == "torch" and not snake_moved:
            print("Actually Smart, wow\nThey get scared and Door Opens")
            snake_moved = True#Can you have 2x  equals?>>>>>>>YOU CANNOT IT DOES NOT WORK

        elif choice == "torch" and  snake_moved:
            print("They Adapted and killed you")
            dead()

        elif choice == "open" and snake_moved:
            print(f"Nice {user} you were able to go through the door!!")
            gold_room()
        else: 
            print("What do you mean?????")

def gold_room():
    print(f"Welcome Mr {user}, You have finally reached your destination!")
    print("So how much gold do you want?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(input())
    else:
        dead()
    if choice < 100:
        print("Congrats you are not a greedy fuck!")
        exit(0)

    elif choice > 101:
        print("I will give it to you but if it was any higher You be Gonzo")
        exit(0)
    else:
        print("Learn to write a number you beach!!")
        gold_room()



start()
