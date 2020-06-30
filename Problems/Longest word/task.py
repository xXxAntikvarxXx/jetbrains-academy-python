word1 = input()
word2 = input()

# How many letters does the longest word contain?
print(len(word1) if len(word1) > len(word2) else len(word2))
