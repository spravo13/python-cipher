#!/usr/bin/python3.4
"""Check remainder from alphabet and rearrange letters based on outcome"""

PIN = int(input("Enter your number: "))
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
REMAINDER = PIN % 26
FIRST_LETTER = 27 - REMAINDER

if REMAINDER == 0:
    #Keep array to kjust alphabet
    LETTERS = LETTERS
else:
    #Shift alphabet based on remainder of pin
    NUMBERS = list(range(FIRST_LETTER, 27))
    COUNT = 0
    for NUMBER in NUMBERS:
        LETTERS.insert(COUNT, LETTERS[NUMBER-1])
        del LETTERS[NUMBER]
        COUNT = COUNT + 1

#Turn typed in message into a list and all lowercase
MESSAGE = list(input("Enter your message: ").lower())

print(LETTERS)
print(MESSAGE)
