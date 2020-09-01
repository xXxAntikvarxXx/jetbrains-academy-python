class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    pass


seine = River("Seine", 777)
