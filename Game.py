playing_field = [["1 ", "—", "—", "—", ""],
                 ["2 ", "—", "—", "—", ""],
                 ["3 ", "—", "—", "—", ""],
                 ["   1 2 3"]]


def result(field: list) -> bool:
    result_bool = False
    for i in field:
        if i.count("X") == 3:
            result_bool = True
        if i.count("O") == 3:
            result_bool = True
    for j in range(3):
        col = [field[i][j] for i in range(3)]
        if col.count("X") == 3:
            result_bool = True
        if col.count("O") == 3:
            result_bool = True
    diag1 = [field[i][i+1] for i in range(3)]
    diag2 = [field[i][3-i] for i in range(3)]
    if diag1.count("X") == 3 or diag2.count("X") == 3:\
        result_bool = True
    if diag1.count("O") == 3 or diag2.count("O") == 3: \
            result_bool = True
    return result_bool


def draw(field: list) -> bool:
    x = 0
    draw_bool = False
    for row in field:
        if "—" not in row:
            x += 1
        if x == 4:
            draw_bool = True
    return draw_bool


def free_cell(field: list, row: int, col: int):
    while True:
        if field[row-1][col] == "X" or playing_field[row-1][col] == "O":
            print("Еблан?")
            row, col = map(int, input("Повтори ход:").split())
            continue
        else:
            return row, col


while True:
    x, y = map(int, input("Игрок 1:").split())
    x, y = free_cell(playing_field, x, y)
    playing_field[x-1][y] = "X"
    for row in playing_field:
        print(*row, sep="|")
    if result(playing_field):
        print("Игрок 1 победил")
        break
    if draw(playing_field):
        print("Ничья")
        break

    x, y = map(int, input("Игрок 2:").split())
    x, y = free_cell(playing_field, x, y)
    playing_field[x - 1][y] = "O"
    for row in playing_field:
        print(*row, sep="|")
    if result(playing_field):
        print("Игрок 2 победил")
        break
    if draw(playing_field):
        print("Ничья")
        break
