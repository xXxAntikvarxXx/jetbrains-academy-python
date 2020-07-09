cats_cafe = max((
    cafe.split()
    for cafe in iter(input, "MEOW")
), key=(lambda x: int(x[1])))

print(cats_cafe[0])
