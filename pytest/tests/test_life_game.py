from app.life_game import generate_board, Cell

def test_initial_grid():

    board = generate_board(".X\n..")
    # set
    mock_board = set()

    assert mock_board  == board