# place `import` statement at top of the program
from math import copysign

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))

print(str(copysign(x, y)))
