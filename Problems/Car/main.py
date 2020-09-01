class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    pass


# create an instance of Tesla
tesla_car = Tesla("S", "black")
