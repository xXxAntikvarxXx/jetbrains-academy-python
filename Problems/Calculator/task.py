# put your python code here
a = float(input())
b = float(input())
op = input()

if op in ["/", "mod", "div"] and b == 0:
    print("Division by 0!")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "/":
    print(a / b)
elif op == "*":
    print(a * b)
elif op == "mod":
    print(a % b)
elif op == "pow":
    print(a ** b)
elif op == "div":
    print(a // b)
