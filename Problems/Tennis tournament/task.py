n = int(input())
players = [input().split(" ") for _ in range(n)]
win = [player[0] for player in players if player[1] == "win"]
print(win)
print(len(win))
