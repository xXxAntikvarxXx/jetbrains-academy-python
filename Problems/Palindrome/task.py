word = input()

# print("Palindrome" if word == word[::-1] else "Not palindrome")
print("Not palindrome"[4 * (word == word[::-1])::].capitalize())
