class MyClass:
    n_objects = 0

    def __new__(cls, *args, **kwargs):
        if cls.n_objects < 5:
            cls.n_objects += 1
            return object.__new__(cls)
        return None

    def __str__(self):
        return "An object of MyClass"
