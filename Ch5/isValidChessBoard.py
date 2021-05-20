board = {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "6h": "bqueen", "3e": "wking"}


def is_valid_chess_board(board):
    valid_piece_colors = ("w", "b")
    pieces = ("pawn", "king", "bishop", "rook", "queen")
    valid_chess_pieces = []
    valid_chess_positions = []
    for piece in pieces:
        for col in valid_piece_colors:
            valid_chess_pieces.append(col + piece)

    for i in range(1, 9):
        for j in range(1, 9):
            valid_chess_positions.append(str(i) + chr(96 + j))
    board_positions = list(board.keys())
    board_pieces = list(board.values())
    check_pos = [pos for pos in board_positions if pos not in valid_chess_positions]
    check_pcs = [piece for piece in board_pieces if piece not in valid_chess_pieces]

    if check_pcs != [] or check_pos != []:
        return False
    return True


print(is_valid_chess_board(board))
