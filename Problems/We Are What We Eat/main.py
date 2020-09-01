# the list "meals" is already defined
# your code here
kcal = sum(meal.get('kcal', 0) for meal in meals)
print(kcal)
