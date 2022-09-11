

from random import randint
import re
from secrets import choice


class Scene(object):
    def enter(self):
        print("TBH I DON'T KNOW WHAT ENTER IS \n Look at the top and see what this is!")
        exit(1)#safe release

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
#2
class Death(Scene):
    quips = [
        "You died. you kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such as luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]


    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])

class CentralCorridor(Scene):

    def enter(self):
        print("Welcome To the ship Dear Comrade!\n You are currently located in the central corridor of x23f sector")
        print("------------------------\n")
        print("You come across the pred, what do you do?")
        print("1.shoot/2.run/3.hug")

        choice = input("> ")

        if choice == "shoot":
            print("You shot 5 rounds of the mag, but missed all shots\nwhile reloading you got taken")

            return 'death'

        elif choice == 'run':
            print("You decided to run away like a beach but like a loser you stumbled\n soo predictable...")

            return 'death'
        elif choice == "hug":
            print("This was a clear bait, but you did not fall for it\n nice You go next stage!!")

            return 'laser_weapon'

        else:
            print("what the freak you mean twin?")

            return 'central_corridor'
        



class LaserWeaponArmory(Scene):

    def enter(self):

        print("There is a lock to get to the room to access the explosivee...\nTry Guessing it, it's a 1 pin code!")

        code = f"{randint(0,9)}"
        guess = input("[Pin Code] >")
        guesses = 0


        while guess != code and guesses < 10:
           guesses =+ 1
           print("Failed!>Try Again!")

           guess = input("[Pin Code] >")

        if guess == code:
            print("Congrats Mister!\nYou have managed bypass the security") 
            print("You can now access the bomba")

            return 'the_bridge'
        
        else:
            print("Write a damn number ur muppet that get's it done!")
            print("Good bye")

            return 'death'

            

        

class TheBridge(Scene):
    def enter(self):
        print("After getting the explosives, you reach the bridge but some clowns are in front of you.")
        print("Do you? 1. 'negotiate' with your life\n2.'start' the bomb\n3.'surrender'so you could run when they don't see u")

        choice = input("> ")
        if "negotiate" in choice:
            print("R u Dumb?\n they clowns and troll\n Gunzo")
            return 'death'
        elif "start" in choice:
            print("Well done, they got jebaited as they ran away thinking it would explode but you could turn it off.")
            return 'escape_pod'
        else:
            print("You Cow beach ass. BBEGONE")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print("You have the chance to escape. but as DBZ Capsules...\nChoose between 3 Capsules and might live..")
        
        choice = input("> ")

        guess = f"{randint(1,4)}"


        if int(choice) == guess:
            print('Great Job\nYou survived another day in your adventure...\nTO BE CONTINUED....')
            return 'finished'

        else:
            print("You entered the capsul, just to realise it doesnt work and now your stuck untill it explodes...")
            return 'death'

class Finished():
    def enter(self):
        print("You Won....")
        return 'finished'

class Map(object):

    scenes = {
        
        'central_corridor': CentralCorridor(),
        'laser_weapon': LaserWeaponArmory(),
        'death': Death(),
        'finished': Finished(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod()


    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):

        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_Map = Map('central_corridor')
a_Map = Engine(a_Map)
a_Map.play()