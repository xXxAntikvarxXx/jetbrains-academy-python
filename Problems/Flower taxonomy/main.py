iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {
        **{"species": species,
           "petal_length": petal_length,
           "petal_width": petal_width},
        **kwargs
    }
