class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def runSong(self):
        for line in self.lyrics:
            print(line)


## THIS IS AN INSTANCE 
"-------------------------------------------------------"
happy_dbay = Song(["Happy birthday to you",
"I don't want to get sued", "So i'll stop right here!"])

bulls_on_parade = Song(["They rally around the family",
 "With pockets full of shells"])
"-------------------------------------------------------"

# lol = happy_dbay.lyrics
# print(lol)
happy_dbay.runSong()

bulls_on_parade.runSong()


# class Emplyees():


#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.forecastCalculator = self.pay * 3


#  #Alot of data here:
# customer1 = Emplyees("Bob", "Lanny", 50000)
# customer2 = Emplyees("Curry", "Lane", 10000)

# print(customer1.first)
# print(customer2.forecastCalculator)

#print("Hello")