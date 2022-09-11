

from random import randint


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
         pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Finished():
    pass

class Map(object):

    scenes = {
        
        'central_corridor': CentralCorridor(),
        'laser_weapon': LaserWeaponArmory(),
        'death': Death(),
        'finished': Finished()


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