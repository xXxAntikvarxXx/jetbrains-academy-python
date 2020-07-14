# Write your code here
import random


print("H A N G M A N")
WORDS = ['python', 'java', 'kotlin', 'javascript']
WIN_WORD = random.choice(WORDS)
word = input("Guess the word: > ")
if word == WIN_WORD:
    print("You survived!")
else:
    print("You are hanged!")
