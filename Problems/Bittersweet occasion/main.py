# finish the function
def find_the_parent(child):
    if issubclass(child, Drinks):
        print("Drinks")
    elif issubclass(child, Pastry):
        print("Pastry")
    elif issubclass(child, Sweets):
        print("Sweets")
