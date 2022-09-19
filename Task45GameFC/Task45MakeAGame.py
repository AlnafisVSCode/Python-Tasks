"""
- Create a character? -> creates an instance of a function Character
    - Save info on the charac on a var?


>IMPORT
    -Use Different files to work with.

>COMPOSITION

>INHERITANCE

>DICTIONARIES

>Save File

>Read File

>Lists




STORY:
    :Football 
        - Team
        - Player
        - goals
        - wins
        - loses
    : Ratings (randint)
    : Wage
    : Retire
"""



import Teams


arrow = "> "
class User():
    
    def __init__(self, start):
        self.start = start()

    

    def start():
        print("----->>>>________Welcome To The Football Game!_________<<<<<<-----")
        print("|                                                                |")
        print("|                                                                |")
        print("|                   You could Win $100,000,000                   |")
        print("|                                                                |")
        print("|                                                                |")
        print("|                                                                |")
        print("|________________________________________________________________|\n")

        print("Hello Dear Player!-----> What is your Name?")
        user_name = input(arrow)
        print(user_name,"Nice to meet you!\n>>Pick a team from the list you want them to win!")

        for fc in list(Teams.FCTeams):

            # count = Teams.FCClubs(fc)
            # print(f"{fc} : {count}"
            print(f"{fc}")



User.start()

