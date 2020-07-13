# write your code here
# Working with string
# cells = input()
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
# straights = [
#     # rows
#     cells[:3], cells[3:6], cells[6:],
#     # columns
#     cells[0:9:3], cells[1:9:3], cells[2:9:3],
#     # diagonals
#     cells[0:9:4], cells[2:7:2]
# ]
# # print fields
# print('---------')
# print('|', ' '.join(cells[:3]), '|')
# print('|', ' '.join(cells[3:6]), '|')
# print('|', ' '.join(cells[6:]), '|')
# print('---------')
#
# if (
#     abs(cells.count('X') - cells.count('O')) > 1 or
#     ('XXX' in straights and 'OOO' in straights)
# ):
#     print('Impossible')
# elif 'XXX' in straights:
#     print('X wins')
# elif 'OOO' in straights:
#     print('O wins')
# elif cells.count('_') > 0:
#     print('Game not finished')
# else:
#     print('Draw')

# Working with matrix
cells = list(input())
cells = [cells[i:i + 3] for i in range(0, len(cells), 3)]


def print_fields(fields):
    print("---------")
    for row in fields:
        print(f"| {' '.join(row)} |")
    print("---------")


def win(fields, val):
    fill = [val, val, val]
    return (
        fill in fields or
        fill in [[
            fields[0][0], fields[1][1], fields[2][2]
        ], [
            fields[0][2], fields[1][1], fields[2][0]
        ]] or
        any(
            fill == [fields[0][i], fields[1][i], fields[2][i]]
            for i in range(len(fields))
        )
    )


def empty_cell(fields):
    return any(
        ("_" in row or " " in row) for row in fields
    )


def count_cell(fields, val):
    return sum(
        sum(cell == val for cell in row)
        for row in fields
    )


X_wins = win(cells, "X")
X_count = count_cell(cells, "X")
O_wins = win(cells, "O")
O_count = count_cell(cells, "O")
empty = empty_cell(cells)

print_fields(cells)

if (X_wins and O_wins) or (abs(X_count - O_count) > 1):
    print("Impossible")
elif X_wins:
    print("X wins")
elif O_wins:
    print("O wins")
elif empty:
    print("Game not finished")
else:
    print("Draw")
