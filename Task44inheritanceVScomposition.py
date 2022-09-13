''' Basic Def of Inheritance


class Parent():

    def implicit(self):
        print("Parent imPlicit()")

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()'''

"----------------------------------"


# class Child():
#     def overrid4e(self):
#         print("Child OverRide()")

# class Parent(Child):
#     def override(self):
#         print("Parent OverRide()")





# dad = Parent()
# son = Child()

# dad.overrid4e()
# son.overrid4e()


"------------------------------------------------"
"SUPEEEEEEEEEEER"
# class Parent():

#     def altered(self):
#         print("Parent altered()")

# class Child(Parent):
#     def altered(self):
#         print("Child, before parent altered()")
#         super(Child, self).altered()
#         print("Child, After parent altered()")
        

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()


"-----------------------------------------------------------"
"The Whole thing SOLO"
class Parent():

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


print("-------------------------------------------------")

class Parent():
    def overide(self):
        print("Parent OverrIde()")

class Child(Parent):
    def overidee(self):
        print("Child override()")

dad = Parent()
son = Child()


dad.overide()
son.overidee()


print("---------------------------------------------------------")

class Parent():
    def altered(self):
        print("Parent Alltered!")

class Child(Parent):
    def altered(self):
        print("Child before Parent Altered()")
        super(Child, self).altered()
        print("Child, after Parent Altered()")

dad = Parent()

son = Child()


dad.altered()

son.altered()
