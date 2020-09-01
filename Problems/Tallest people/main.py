def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    people = [
        (name, height)
        for name, height in kwargs.items()
        if height == max_height
    ]
    people.sort(key=lambda person: person[0])
    for name, height in people:
        print(f"{name} : {height}")
