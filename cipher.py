#!/usr/bin/python3.4
"""Check remainder from alphabet and rearrange letters based on outcome"""

CODE = int(input("Enter your number: "))

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
REMAINDER = CODE % 26
FIRST_LETTER = 27 - REMAINDER

if REMAINDER == 0:
    LETTERS = LETTERS
else:
    NUMBERS = list(range(FIRST_LETTER, 27))
    COUNT = 0
    for NUMBER in NUMBERS:
        LETTERS.insert(COUNT, LETTERS[NUMBER-1])
        del LETTERS[NUMBER]
        COUNT = COUNT + 1

print(LETTERS)
