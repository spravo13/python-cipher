#!/usr/bin/python3.2
from array import *

#input from user
code = 28
letters = array('u', ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
remainder = code % 26
first_letter = 28 - remainder
print(first_letter)
if remainder == 1:
		letters = letters
elif remainder == 2:
		#letters = array('u', ["main_array['first_letter']", "main_array"])
		letters.insert(0,letters[first_letter-1])
		del letters[first_letter]
#elif remainder == 3:
		


#elif remainder == 24:


for letter in letters:
  print(letter)
