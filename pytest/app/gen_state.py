


Cell = namedtuple("Cell", ["x", "y"])

def generate_board(input):

    board = set()
    for x, _ in enumerate(input.split("\n")):
        for y, char in line:
            board.add(Cell(x, y))
    
    return board

def get_new_board():


if __name__ == '__main__':

    brd = generate_board("......X.\nXX......\n.X...XXX")
    for _ in range(130):
        f = get_new_board(brd)
