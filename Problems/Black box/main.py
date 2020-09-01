# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]
print(
    "modifies" if id(lst) == id(blackbox(lst)) else "new"
)
