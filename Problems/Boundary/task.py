# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = list(filter((lambda x: x < 5), numbers))
greater_than_5 = list(filter((lambda x: x > 5), numbers))

# printing your results
print(less_than_5)
print(greater_than_5)
