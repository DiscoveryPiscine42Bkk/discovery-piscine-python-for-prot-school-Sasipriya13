def checkmate(board):
    """ตรวจสอบว่า King อยู่ในสถานะ check หรือไม่"""
    # แปลงบอร์ดเป็นแถวๆ
    board = board.strip().splitlines()
    n = len(board)

    # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมหรือไม่
    if any(len(row) != n for row in board):
        print("Error")
        return

    # ค้นหาตำแหน่งของ King
    king_position = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break
    
    # ถ้าไม่พบ King ในกระดาน
    if not king_position:
        print("Error")
        return

    king_x, king_y = king_position

    # ทิศทางการโจมตีของหมากต่างๆ
    directions_rook_queen = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # แนวตั้งและแนวนอน
    directions_bishop_queen = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # ทแยงมุม
    directions_pawn = [(-1, -1), (-1, 1)]  # การโจมตีของ Pawn ทแยงมุม

    # ฟังก์ชันการตรวจสอบการโจมตีจาก Pawn
    def check_pawn(x, y):
        for dx, dy in directions_pawn:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'K':
                return True
        return False

    # ฟังก์ชันการตรวจสอบการโจมตีจาก Rook หรือ Queen
    def check_rook_or_queen(x, y, directions):
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < n:
                nx += dx
                ny += dy
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'K':
                        return True
                    if board[nx][ny] != '.':
                        break
        return False

    # ตรวจสอบการโจมตีจากหมากต่างๆ
    for i in range(n):
        for j in range(n):
            piece = board[i][j]
            if piece == '.':
                continue
            if piece == 'P':  # ตรวจสอบ Pawn
                if check_pawn(i, j):
                    print("Success")
                    return
            elif piece == 'B' or piece == 'Q':  # ตรวจสอบ Bishop หรือ Queen
                if check_rook_or_queen(i, j, directions_bishop_queen):
                    print("Success")
                    return
            elif piece == 'R' or piece == 'Q':  # ตรวจสอบ Rook หรือ Queen
                if check_rook_or_queen(i, j, directions_rook_queen):
                    print("Success")
                    return
    
    # ถ้าไม่มีหมากที่สามารถโจมตี King
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