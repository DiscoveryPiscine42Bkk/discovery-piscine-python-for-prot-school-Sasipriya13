def checkmate(board: str):
    # แปลงกระดานจาก string เป็น 2D list
    board = [list(row) for row in board.splitlines()]
    n = len(board)  # ขนาดของกระดาน (กระดานเป็นสี่เหลี่ยมจึงมีขนาดเท่ากันทั้งแถวและคอลัมน์)
    
    # หาตำแหน่งของ King
    king_position = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    # ถ้าไม่พบ King หรือพบมากกว่าหนึ่ง King พิมพ์ Error
    if not king_position:
        print("Error")
        return

    # ทิศทางการโจมตีของชิ้นส่วนต่างๆ
    directions = {
        'P': [(-1, -1), (-1, 1)],  # Pawn โจมตีทแยงมุม
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop โจมตีทแยงมุม
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook โจมตีในแนวตั้งและแนวนอน
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # Queen โจมตีทั้งในแนว Rook และ Bishop
    }

    # ฟังก์ชันตรวจสอบตำแหน่งว่าคือในขอบเขตของกระดานหรือไม่
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    # ฟังก์ชันตรวจสอบว่าชิ้นส่วนสามารถโจมตี King ได้หรือไม่
    def check_attack(piece, x, y, dx, dy):
        while in_bounds(x + dx, y + dy):
            x += dx
            y += dy
            if board[x][y] != '.':
                if board[x][y] == piece:
                    return True
                break
        return False

    # ตำแหน่งของ King
    x, y = king_position

    # ตรวจสอบทุกทิศทางว่า King ถูกโจมตีหรือไม่
    for piece, dirs in directions.items():
        for dx, dy in dirs:
            if check_attack(piece, x, y, dx, dy):
                print("Success")
                return
    
    print("Fail")

def main():
    # ตัวอย่าง 1: King ถูกโจมตี
    board = """\
R...
.K..
..P.
...."""
    checkmate(board)

    # ตัวอย่าง 2: King ไม่ถูกโจมตี
    board = """\
.. 
.K"""
    checkmate(board)

if __name__ == "__main__":
    main()