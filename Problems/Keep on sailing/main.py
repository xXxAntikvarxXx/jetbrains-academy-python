# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, dest):
        return f"The {self.name} has sailed for {dest}!"


black_pearl = Ship("Black Pearl", 800)
print(black_pearl.sail(input()))
