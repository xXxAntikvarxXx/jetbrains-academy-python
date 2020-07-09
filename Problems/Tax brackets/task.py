money = int(input())

if money <= 15527:
    percent = 0
elif money <= 42707:
    percent = 15
elif money <= 132406:
    percent = 25
else:
    percent = 28

print(f"The tax for {money} is {percent}%. "
      f"That is {int(round(money * percent / 100.0))} dollars!")
