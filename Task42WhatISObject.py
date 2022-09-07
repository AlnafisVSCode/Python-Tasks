#There you have it: Mary is a kind of salmon that is a kind of fish—object is a class is a class.

##Animal is a object (yes), look at extra credit...
class Animal():
    pass


##Class dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##from self get name attribute and set it to name
        self.name = name

##Class Cat is-a Animal
class Cat(Animal):
    def __init__(self, name): 
        ##from self get name attribute and set it to name
        self.name = name
##Make a class called person
class Person():
    def __init__(self, name):
        ##from self get name and set it to name
        self.name = name
        ##Person has-a pet of some kind-------------------------
        self.pet = None

##Class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##hmm what is this strange magic?
        super(Employee, self).__init__(name)

        ##from self get salary and set it to salary
        self.salary = salary

##class Fish 
class Fish():
    pass

##class salmon is-a Fish
class Salmon(Fish):
    pass

##class halibut is-a inheratnce of class fish
class Halibut(Fish):
    pass

## Rover is a dog
rover = Dog("Rover")

##satan calls an instance of class Cat that takes Satan as params
satan = Cat("Satan")

##Mary calls an instance of class Person which takes mary as params
mary = Person("Mary")

##from mary get pet attribute and set it to satan
mary.pet = satan

##frank calls an instance of class Emplyee that takes Frank and 120 as params
frank = Employee("Frank", 120000)

##from frank get pet attribute and set it to rover
frank.pet = rover

##flipper calls class Fish
flipper = Fish()
##crouse calls an instance of class Salmon
crouse = Salmon()
##harry calls an instance of class Halibut
harry = Halibut()

