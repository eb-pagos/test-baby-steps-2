from collections import namedtuple, defaultdict
import time

Cell = namedtuple("Cell", ["x", "y"])


def get_neighbors(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)


def get_neighbor_count(board):
    neighbor_counts = defaultdict(int)
    for cell in board:
        for neighbor in get_neighbors(cell):
            neighbor_counts[neighbor] += 1
    return neighbor_counts


def advanced_board(board):
    new_board = set()
    for cell, count in get_neighbor_count(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board


def generate_board(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "X":
                board.add(Cell(int(col), int(row)))
    return board


def board_to_string(board, pad=0):
    if not board:
        return "empty"
    board_str = ""
    xs = [x for (x, _) in board]
    ys = [y for (_, y) in board]
    for y in range(min(ys) - pad, max(ys) + 1 + pad):
        for x in range(min(xs) - pad, max(xs) + 1 + pad):
            board_str += "X" if Cell(x, y) in board else "."
        board_str += "\n"
    return board_str.strip()


if __name__ == "__main__":
    f = generate_board("......X.\nXX......\n.X...XXX")
    for _ in range(5):
        f = advanceBoard(f)
        print(boardToString(f, 2))
        print("--")
        time.sleep(0.1)
