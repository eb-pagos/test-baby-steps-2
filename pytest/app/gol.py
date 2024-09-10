from collections import namedtuple


Cell = namedtuple("Cell", ["x", "y", "status", "neighbor"])
def initialize_board(input):
    board = set()
    for x, linex in enumerate(input.split("\n")):
        for y, status in enumerate(linex):
            board.add(Cell(x=x, y=y, status=status))
    return board


def get_neighbors(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)

def build_new_board(bord):
    for cell in board:


class Cell {
    const x;
    const y;
}