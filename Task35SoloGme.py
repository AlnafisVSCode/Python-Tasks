#gold room
#Trap Door
#snake_room
#Dead
#Start


user = input("Hello User, What is your name ?")

def start():
    # print("Hello User, What is your name ?", end= "")
    # user = input()
    print(user, "you are in a cave!\nYou Have 2 Choices 'Left' or 'Right'")

    choice = input(f"{user}: ")

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
    print("1.'Run' for it?\n2.'Hit' the snakes?\n3.'Use the 'Torch' to scare the snakes?")

    snake_moved = False

    while True:
        








snake_room()