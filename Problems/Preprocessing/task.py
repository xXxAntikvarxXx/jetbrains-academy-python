string = input()
length = len(string)
string = string.replace(',', '', length + 1)
string = string.replace('.', '', length + 1)
string = string.replace('?', '', length + 1)
string = string.replace('!', '', length + 1)
print(string.lower())
