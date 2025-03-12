def checkmate(board):
    board = [list(row) for row in board.splitlines()]
    king_pos = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    if not king_pos:
        return  
    king_x, king_y = king_pos
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    def check_rook_or_queen(x, y, dx, dy, piece):
        while 0 <= x < len(board) and 0 <= y < len(board):
            if board[x][y] == piece:
                return True
            if board[x][y] != '.':
                break
            x += dx
            y += dy
        return False
    diagonal_directions = [
        (1, 1),   
        (-1, 1),  
        (1, -1),  
        (-1, -1)  
    ]
    def check_bishop_or_queen(x, y, dx, dy, piece):
        while 0 <= x < len(board) and 0 <= y < len(board):
            if board[x][y] == piece:
                return True
            if board[x][y] != '.':
                break  
            x += dx
            y += dy
        return False
    def check_pawn(x, y):
        if 0 <= x < len(board) and 0 <= y < len(board):
            return board[x][y] == 'P'
        return False
    for dx, dy in directions:
        if check_rook_or_queen(king_x + dx, king_y + dy, dx, dy, 'R') or check_rook_or_queen(king_x + dx, king_y + dy, dx, dy, 'Q'):
            print("Success")
            return
    for dx, dy in diagonal_directions:
        if check_bishop_or_queen(king_x + dx, king_y + dy, dx, dy, 'B') or check_bishop_or_queen(king_x + dx, king_y + dy, dx, dy, 'Q'):
            print("Success")
            return
    for dx, dy in [(-1, -1), (-1, 1)]:
        if check_pawn(king_x + dx, king_y + dy):
            print("Success")
            return
    print("Fail")
def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
if __name__ == "__main__":
    main()