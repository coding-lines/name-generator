from random import choice

vowels = list("aeiou")
consonants = list("wrtzupsdfghjklycvbnm")
beginning = list('QWERTZUIOPLKJHGFDSAYXCVBNM')

def newName():
    return choice(beginning)+choice([choice(consonants),choice(vowels)])
    #Return the first two letters, which will be chosen randomly

def continueName(name):
    if list(name)[len(list(name))-1] in vowels:
        return name + choice(consonants)
        #Use consonant, if the last letter is a vowel
    elif list(name)[len(list(name))-2] in vowels:
        return name + choice([choice(vowels), choice(consonants)])
        #Use either consonant or vowel, if the second-last letter is a vowel
    else:
        return name + choice(vowels)
        #Use vowel, if there is no vowel in the last two letters

def createNameOfLength(length):
  name = newName()
  for i in range(int(length)-2):
    name = continueName(name)
  return name
