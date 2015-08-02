#!/usr/bin/python3.4
"""Check remainder from alphabet and rearrange letters based on outcome"""

PIN = int(input("Enter your number: "))
ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
REMAINDER = PIN % 26
FIRST_LETTER = 27 - REMAINDER

if REMAINDER == 0:
    #Keep array to just alphabet
    LETTERS = LETTERS
else:
    #Shift alphabet based on remainder of pin
    NUMBERS = list(range(FIRST_LETTER, 27))
    COUNT = 0
    for NUMBER in NUMBERS:
        LETTERS.insert(COUNT, LETTERS[NUMBER-1])
        del LETTERS[NUMBER]
        COUNT = COUNT + 1

#Turn message into a list and all lowercase
MESSAGE = list(input("Enter your message: ").lower())

#Encode message to numbers
if MESSAGE != "":
    #Create empty list for the string encoded to numbers
    NUMBER_ENCODED = []
    for LETTER in MESSAGE:
        #Add each number that comes from the letter to the list
        NUMBER_ENCODED.append(ALPHABET.index(LETTER))

#Encode message to scrambled words
#Create empty list for the encoded numbers to go to the encode message
MESSAGE_ENCODED = []
for NUMBER in NUMBER_ENCODED:
    #Add each letter that corrisponds to the number in the LETTERS list
    MESSAGE_ENCODED.append(LETTERS[NUMBER])

ENCODED_STRING = ''.join(str(l) for l in MESSAGE_ENCODED)

print(ENCODED_STRING)
