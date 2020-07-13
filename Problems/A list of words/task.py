# work with the preset variable `words`
# print([word for word in words if word.startswith(("a", "A"))])
# print([word for word in words if word[0] in "aA")
# print([word for word in words if word.lower() == "a")
print([word for word in words if word.lower().startswith("a")])
