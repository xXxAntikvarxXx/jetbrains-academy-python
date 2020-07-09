scores = input().split()
# put your python code here
correct = 0
incorrect = 0
for score in scores:
    if incorrect == 3:
        break
    correct += int(score == "C")
    incorrect += int(score == "I")

print("Game over" if incorrect == 3 else "You won")
print(correct)
