"https://rupert.id.au/python/book/learn-python3-the-hard-way-nov-15-2018.pdf"
"163 pg"





"1==1 == False - Wrong"
"1==1 =  Works"







# def assert_this(arg1,arg2):
#     print("Are you Asserting this?")
#     print(f"Are1 is {arg1} and arg2 is {arg2}")
#     # assert True, "Error"
    


# assert_this(1,2)








from re import I


arrow = "> "
# def Duungeon():
#     print("Welcome to the game that feels never ending!")
#     print("Guess the number to go to level 2 or FF")
#     up_five = ["1","2","3","4","5"]
#     down_five = 1, 2, 3
#     loop = False
#     x = 6

#     while True:
#         print("\nRANGE FROM : 1 - 10")

#         choice = int(input(arrow))
#         if choice == x:
#             print("GAMEOVER------------------------------------------>")
#             dead()
#         elif choice == 9 and not loop:
#             print("Nice One. You can Proceed to Lv 2.")
#             print("jk")
#             loop = True
#         elif choice == 9 and loop:
#             print("Nice One. You can Proceed to Lv 2.")
#             level_2()
#             break
#         # elif choice != 9:
#         #     print("You Lost\n GO Again!..?")

#         else:
#             print("Go Aggane")
#         # else:
#         #     print("You Lost\n GO Again!..?")
#         #     break
    
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
            # continue
            # level_3()

        else:
            print("I think that's not the range we asked you Asshole!")


def if_statement():
    1 == 1 == False
            

if_statement()

def dead():
    print("gOne")

level_2()
def level_3():
    print("Welcome to Level 3")


Duungeon()


print( "Hello \a hello\r")




