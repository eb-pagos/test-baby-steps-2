from app.life_game import generate_board, Cell

def test_initial_grid():

    board = generate_board(".X\n..")
    mock_sell = Cell()
    mock_board = set(mock_sell)

    assert board.size() ==  1


def 