# put your python code here
days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

print(
    days * food_cost + flight_cost * 2 + hotel_cost * (days - 1)
)
