# If the user typed ”run”, and exactly ”run, then the game worked. If they typed in similar phrases like ”run fast” it would fail.

#Create a Module to be more english

#In our game we have to create a list of allowable words called a ”lexicon”:


import re


stuff = input('> ')
words = stuff.split()

# print(words)

# list1 = [words]

# print(list1[0])

##  Lexicon Tuples

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = (first_word, second_word, third_word)
# print(sentence)

####    Try exception and numbers

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None