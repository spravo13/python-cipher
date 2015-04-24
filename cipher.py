#!/usr/bin/python3.2
from array import *

code = int(input('Enter your number: '))
letters = array('u', ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
remainder = code % 26
first_letter = 27 - remainder
if remainder == 0:
    letters = letters
else:
    numbers = list(range(first_letter,27))
    start = 0
    for number in numbers:
        letters.insert(start,letters[number-1])
        del letters[number]
        start = start + 1

for letter in letters:
    print(letter)
