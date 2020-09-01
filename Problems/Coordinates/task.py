x = float(input())
y = float(input())


if x > 0:
    if y > 0:
        print("I")
    elif y < 0:
        print("IV")
elif x < 0:
    if y > 0:
        print("II")
    elif y < 0:
        print("III")
