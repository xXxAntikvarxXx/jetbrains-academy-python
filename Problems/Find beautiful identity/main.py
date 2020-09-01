def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if id(i) % 1000 == 888:
            return i
    return None
