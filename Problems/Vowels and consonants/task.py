consonant = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"

word = input()

for letter in word:
    if letter in vowel:
        print("vowel")
    elif letter in consonant:
        print("consonant")
    else:
        break
