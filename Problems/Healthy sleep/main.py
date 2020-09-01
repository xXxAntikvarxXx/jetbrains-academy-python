a, b, h = (int(input()) for _ in range(3))
msg = "Deficiency" if h < a else (
    "Excess" if h > b else "Normal"
)
print(msg)
