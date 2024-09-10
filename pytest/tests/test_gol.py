
# from app.gol import Cell, initialize_board

# def test_initialize_board_pass():
#     board_input = ".x\n.x"
#     board = initialize_board(board_input)
#     cell_list = [Cell(x=0, y=0, status="."), Cell(x=1, y=0, status="."), Cell(x=0, y=1, status="x"), Cell(x=1, y=1, status="x")]
#     mock_board = set(cell_list)
#     assert mock_board == board


# def test_get_neighbors():
#     board_input = ".x\nx.\n.."
#     board = initialize_board(board_input)
#     mock_neighbor = set(CellX(x=1, y=1, status='.', neighbor=set()))
#     neighbor = get_neighbors(board, x=1, y=1)
#     assert mock_neighbor == neighbor
