from random import choice

vowels = list("aeiou")
consonants = list("wrtzupsdfghjklycvbnm")
beginning = list("qwertzuioplkjhgfdsayxcvbnm".upper())

def newName():
    return choice(beginning)+choice([choice(consonants),choice(vowels)])
    #Zwei zufällige Buchstaben

def continueName(name):
    if list(name)[len(list(name))-1] in vowels:
        return name + choice(consonants)
        #Verwendet Konsonant, wenn der letzte Buchstabe ein Vokal ist
    elif list(name)[len(list(name))-2] in vowels:
        return name + choice([choice(vowels), choice(consonants)])
        #Verwendet entweder Konsonant oder Vokal, wenn der zweitletzte Buchstabe ein Vokal ist
    else:
        return name + choice(vowels)
        #Verwendet Vokal, wenn kein Vokal in den letzten zwei Buchstaben

def createNameOfLength(length):
  name = newName()
  for i in range(int(length)-2):
    name = continueName(name)
  return name