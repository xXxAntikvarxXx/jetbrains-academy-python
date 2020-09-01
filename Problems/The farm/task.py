coins = int(input())

if coins >= 6769:
    print(f"{coins // 6769} sheep")
elif coins >= 3848:
    count = coins // 3848
    print(f"{count} {'cow' if count == 1 else 'cows'}")
elif coins >= 1296:
    count = coins // 1296
    print(f"{count} {'pig' if count == 1 else 'pigs'}")
elif coins >= 678:
    count = coins // 678
    print(f"{count} {'goat' if count == 1 else 'goats'}")
elif coins >= 23:
    count = coins // 23
    print(f"{count} {'chicken' if count == 1 else 'chickens'}")
else:
    print(None)
