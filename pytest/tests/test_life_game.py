from app.life_game import generate_board

def test_initial_grid():

    board = generate_board(".X\n..")
    mock_board = set(Cell(x=0, y=0),Cell(x=0, y=1),Cell(x=1, y=0),Cell(x=1, y=1))

    assert mock_board  == board