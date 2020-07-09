"""
camel_case = input()
print(''.join([f'_{i.lower()}' if i.isupper() else i for i in camel_case]))

for c in input():
    print(c if c.islower() else "_" + c.lower(), end="")

text = str(input())
for s in text:
    if s.isupper():
        text = text.replace(s, "_" + s.lower())

print(text)
"""


camel_case = input()
snake_case = ""

for letter in camel_case:
    if letter.isupper():
        letter = "_" + letter.lower()
    snake_case += letter

print(snake_case)
