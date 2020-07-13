n = int(input())

if n < 1:
    print("no army")
elif 1 <= n < 10:
    print("few")
elif 10 <= n < 50:
    print("pack")
elif 50 <= n < 500:
    print("horde")
elif 500 <= n < 1000:
    print("swarm")
else:
    print("legion")
