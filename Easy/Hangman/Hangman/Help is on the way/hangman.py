# Write your code here
import random


print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
win_word = random.choice(words)
word = input(
    f"Guess the word: {win_word[:3] + ('-' * len(win_word[3:]))} > "
)
if word == win_word:
    print("You survived!")
else:
    print("You are hanged!")
