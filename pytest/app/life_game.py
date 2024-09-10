


def generate_board(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "X":
                board.add(Cell(int(col), int(row)))
    return board
