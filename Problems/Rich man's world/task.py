money = int(input().strip())
rate = 0.071  # 7.1% = 7.1 / 100.0
max_deposit = 700000
years = 0

while money < max_deposit:
    # money *= (1 + rate)
    money += money * rate
    years += 1

print(years)
