import sys

# ฟังก์ชันอ่านกระดานหมากรุกจากไฟล์
def read_board_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error")
        sys.exit()

# ฟังก์ชันตรวจสอบความถูกต้องของกระดาน
def validate_board(board):
    # แปลงกระดานเป็นลิสต์ 2D เพื่อให้ง่ายต่อการใช้งาน
    board = [list(row) for row in board.splitlines()]
    n = len(board)
    
    # ตรวจสอบว่าเป็นกระดานสี่เหลี่ยมจัตุรัส
    if any(len(row) != n for row in board):
        print("Error")
        sys.exit()
    
    # นับจำนวนราชา (ต้องมีแค่ 1 ตัว)
    king_count = sum(row.count('K') for row in board)
    if king_count != 1:
        print("Error")
        sys.exit()

    return board

# ฟังก์ชันตรวจสอบว่าอยู่ในสถานะ "เช็ค" หรือไม่
def checkmate(board):
    board = validate_board(board)
    king_r, king_c = find_king(board)
    if king_r is None or king_c is None:
        print("Error")
        sys.exit()
    
    # ตรวจสอบว่าราชาอยู่ในสถานะ "เช็ค" หรือไม่
    if (is_in_check_by_pawn(board, king_r, king_c) or
        is_in_check_by_rook_or_queen(board, king_r, king_c, directions_rook) or
        is_in_check_by_bishop_or_queen(board, king_r, king_c, directions_bishop)):
        print("Success")
    else:
        print("Fail")

# ฟังก์ชันหาตำแหน่งของราชา
def find_king(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                return r, c
    return None, None

# ฟังก์ชันตรวจสอบว่าราชาอยู่ในสถานะ "เช็ค" จาก Pawn หรือไม่
def is_in_check_by_pawn(board, king_r, king_c):
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = king_r + dr, king_c + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'P':
            return True
    return False

# ฟังก์ชันตรวจสอบว่าราชาอยู่ในสถานะ "เช็ค" จาก Rook หรือ Queen (แนวนอน/แนวตั้ง)
def is_in_check_by_rook_or_queen(board, king_r, king_c, directions):
    for dr, dc in directions:
        r, c = king_r, king_c
        while True:
            r += dr
            c += dc
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):  # หากอยู่นอกขอบเขต
                break
            if board[r][c] != '.':
                if (board[r][c] == 'R' or board[r][c] == 'Q'):
                    return True
                break
    return False

# ฟังก์ชันตรวจสอบว่าราชาอยู่ในสถานะ "เช็ค" จาก Bishop หรือ Queen (แนวทแยง)
def is_in_check_by_bishop_or_queen(board, king_r, king_c, directions):
    for dr, dc in directions:
        r, c = king_r, king_c
        while True:
            r += dr
            c += dc
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):  # หากอยู่นอกขอบเขต
                break
            if board[r][c] != '.':
                if (board[r][c] == 'B' or board[r][c] == 'Q'):
                    return True
                break
    return False

# ทิศทางการเคลื่อนที่ของ Rook และ Bishop
directions_rook = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # การเคลื่อนที่ของ Rook
directions_bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # การเคลื่อนที่ของ Bishop
directions_queen = directions_rook + directions_bishop  # Queen เคลื่อนที่ได้ทั้ง Rook และ Bishop

# ฟังก์ชันหลักเพื่อจัดการไฟล์ที่รับเข้ามา
def main():
    if len(sys.argv) < 2:
        print("Error")
        sys.exit()
    
    for filename in sys.argv[1:]:
        board = read_board_from_file(filename)
        checkmate(board)

if __name__ == "__main__":
    main()