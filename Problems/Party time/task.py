guests = []

while True:
    guest = input()
    if guest == ".":
        break
    guests.append(guest)

print(guests)
print(len(guests))
