# def assert_this(arg1,arg2):
#     print("Are you Asserting this?")
#     print(f"Are1 is {arg1} and arg2 is {arg2}")
#     # assert True, "Error"
    


# assert_this(1,2)



arrow = "> "
def Duungeon():
    print("Welcome to the game that feels never ending!")
    print("Guess the number to go to level 2 or FF")
    up_five = ["1","2","3","4","5"]
    down_five = 1, 2, 3
    loop = False
    x = 6

    while True:
        print("\nRANGE FROM : 1 - 10")

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
            break
            # break
        # elif choice != 9:
        #     print("You Lost\n GO Again!..?")

        else:
            print("Go Aggane")
        # else:
        #     print("You Lost\n GO Again!..?")
        #     break
    

def dead():
    print("gOne")

def level_2():
    print("Welcome to level 2")

Duungeon()