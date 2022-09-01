import random


arrow = ">> "


def start():    
    print("Hello Dear User!")   
    print('you can decide for your self to take\nThe Right Path\n\tOr\nThe Left Path')

    choice = input(arrow)
    if choice == "Right":
        print(f"You took the {choice} path\nYou shall enter a dungeon Now....")
        Duungeon()
    elif choice == "Left":
        print(f"You took {choice} path\nYou Skipped to level 2")
        level_2()
    else:
        print("What Frick is Up??\nDead....")
        dead()

#Dungeon
#While loop runs until ITS FALSE
def Duungeon():
    print("Welcome to the game that feels never ending!")
    print("Guess the number to go to level 2 or FF")
    print("RANGE FROM : 1 - 10")
    up_five = ["1","2","3","4","5"]
    down_five = 1, 2, 3
    loop = False
    x = 6

    while True:
        choice = int(input(arrow))
        if choice == x:
            print("GAMEOVER------------------------------------------>")
            dead()
        elif choice == 9 and not loop:
            print("Nice One. You can Proceed to Lv 2.")
            print("jk")
            loop = True
        elif choice == 9 and loop:
            print("Nice One. You can Proceed to Lv 2.")
            level_2()
        elif choice != 9:
            print("You Lost\n GO Again!..?")
        # else:
        #     print("You Lost\n GO Again!..?")
        #     break

    


def level_2():
    
    print(" ")
    print("----->>>>________Welcome To Level 2...________<<<<<<-----")
    print("Welcome to Level 2....")
    print("It's a Math Game\n What is: 2+2+6/2+2+1?")
    for i in range(10):
        choice = int(input(arrow))

        if choice <= 3:
            print("Are you Freaking Dump?")
            
        elif choice <= 6 and choice > 3:
            print("Your Still Dump")
            
        
        elif choice <= 9 and choice >= 6:
            print("Nahhhhhh Cmon Dudeeeeee")
            
        elif choice == 10:
            print("wELL Done...\nUr Smart!")
            level_3()

        else:
            print("I think that's not the range we asked you Asshole!")


def dead():
    print("<<<<<<<<<<<<<YOU ARE GONE>>>>>>>>>>>>>>>")
    exit(0)
    

def level_3():
    print("")
    print("----->>>>________Welcome To Level 3_________<<<<<<-----")
    print("Would you want to leave with 50%' of the loot OR Continue???\n1. Leave\n2. Continue")

    choice = input(arrow)

    for i in range(6):
        
        if "Leave" in choice:
            print("You have decided to leave the game!\n Are you Sure??")
            print("Y/N")

            choice = input(arrow)

            if "Y" in choice:
                print("Well not bad ngl...\n You could have won more but it's safe to go...")
                dead()
            elif "N" in choice:
                print("Ok, you can go back\n")
                level_3()
        elif "Continue" in choice:
            print("You sure are the challenger huh!?\n Well We Will give you a challenge now\n See If you can solve it...\n")
            guess_game()


def guess_game():
    print("----->>>>________Guessing the number_________<<<<<<-----")

    print("Game is quite Simple!\nGuess the number i am thinking of: (x)\n1. Type a Number\n2. '101' for help++You Got 6 Chances\n")
    
    x = 12
    y = False
    z = True

    for i in range(6):

        choice = int(input("> "))

        if choice == 12:
            print("Well Done you have Successfully guessed the number!!!")
            finish_line()
    
        elif choice < 16 and choice != 12:
            print("You are in the right path\nGo Forward!")
            
        elif choice >= 16 and choice <= 100:
            print("You are Definetely NOT in the right path\nGo back")

    
        else:
            print("So You need a Clue I see...")
        
        if choice == 101 and not y and z:
            print("The clue is it's less than 20...")
            y = True
            z = False

        elif choice == 101 and y:
            print("The clue is it's more than 10...")
            y = False
            
        elif choice == 101 and not y:
            print("The clue is it's less than 13...")
    else:
        dead() 
            

def finish_line():
    print("----->>>>________Welcome To The Finish Line!!_________<<<<<<-----")
    print("|                                                                |")
    print("|                                                                |")
    print("|                   You Win $100,000,000                         |")
    print("|                                                                |")
    print("|                    Double or Nothing?                          |")
    print("|                                                                |")
    print("|________________________________________________________________|")

    choice = input("Y/N")

    if "Y" in choice:
        coinToss()
    elif "N" in choice:
        print("----->>>>________Welcome To The Finish Line!!_________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                   You Win $100,000,000                         |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|")
    else: 
        print("What? Y/N*")
        finish_line()


def coinToss():
    print("----->>>>________Welcome To The Coin Flip_________<<<<<<-----")
    print("Do you Choose 'Head' OR 'Tail'")
    choice = input(arrow)
    print("You Chose:", choice)

#0 = head
#1 = tail
    flip = random.randint(0, 1)
    if (flip == 0 and choice == "Head"):
        print("----->>>>__________You WON1 - It was a Head____________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                   You Win $200,000,000                         |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|")

    elif (flip == 0 and choice == "Tail"):
        print("----->>>>__________You LOST - It was a Head____________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                         You Win $0                             |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|")
    
    elif (flip == 1 and choice == "Head"):
        print("You Lose - It was a tail")
        print("----->>>>__________You LOST - It was a Tail____________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                         You Win $0                             |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|")

    elif (flip == 1 and choice == "Tail"):
        print("----->>>>__________You WON2 - It was a Tail____________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                   You Win $200,000,000                         |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|")

    else:
        print("I DONT KNOW WHAT THAT IS.")
        coinToss()
    exit(0)
        

start()



