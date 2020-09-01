class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


shop = Store("GAP", "clothes")
print(shop.name, shop.category)
