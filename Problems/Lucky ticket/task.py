# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = sum(int(d) for d in ticket[:3])
half2 = sum(int(d) for d in ticket[3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
