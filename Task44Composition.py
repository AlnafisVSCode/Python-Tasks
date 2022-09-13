


class Other():

    def override(self):
        print("OTHER Override()")
    
    def implicit(self):
        print("OTHER Implicit()")

    def altered(self):
        print("OTHER altered()")

class Child():

    def __init__(self):
        self.other = Other()


    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):

        print("Child, Before OTHER altered()")

        self.other.altered()

        print("Child, after Other Altered()")
    

son = Child()

son.implicit()
son.override()
son.altered()


 