# write your code here
def print_fields(fields):
    print("---------")
    for row in fields:
        print(f"| {' '.join(row)} |")
    print("---------")


def validate_coordinates(fields, coords):
    try:
        _y = int(coords[0])
        _x = int(coords[1])
    except (ValueError, IndexError):
        return None, None, "You should enter numbers!"
    if _x < 1 or _x > 3 or _y < 1 or _y > 3:
        return None, None, "Coordinates should be from 1 to 3!"
    if fields[3 - _x][_y - 1] != "_":
        return None, None, "This cell is occupied! Choose another one!"
    return _y, _x, None


def update_fields(fields, x, y, val):
    fields[3 - x][y - 1] = val


cells = list(input("Enter cells: > "))
cells = [cells[i:i + 3] for i in range(0, len(cells), 3)]

print_fields(cells)
coordinates = input("Enter the coordinates: > ").split()
coord_y, coord_x, valid = validate_coordinates(cells, coordinates)
while valid is not None:
    print(valid)
    coordinates = input("Enter the coordinates: > ").split()
    coord_y, coord_x, valid = validate_coordinates(cells, coordinates)
update_fields(cells, coord_x, coord_y, "X")
print_fields(cells)
