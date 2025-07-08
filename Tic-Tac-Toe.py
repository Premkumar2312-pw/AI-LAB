import random
def print_board(b):
    print("\nBoard:")
    for r in b:
        print(" | ".join(r))
        print("-"*5)

def check_winner(b, p):
    for i in range(3):
        if all(b[i][j] == p for j in range(3)) or all(b[j][i] == p for j in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3)):
        return True
    return False

def is_draw(b):
    return all(cell != " " for row in b for cell in row)

def get_user_move(b):
    while True:
        try:
            r,c = map(int, input("Enter your move (row col): ").split())
            r -= 1; c -= 1
            if r in range(3) and c in range(3) and b[r][c] == " ":
                return r,c
            print("Invalid move")
        except:
            print("Invalid input")

def get_computer_move(b):
    for p in ['O','X']:
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = p
                    if check_winner(b, p):
                        if p == 'O': return r,c
                        b[r][c] = "O"
                        return r,c
                    b[r][c] = " "
    return random.choice([(r,c) for r in range(3) for c in range(3) if b[r][c] == " "])

def main():
    board = [[" "]*3 for _ in range(3)]
    print("You: X  Computer: O")
    while True:
        print_board(board)
        r,c = get_user_move(board)
        board[r][c] = "X"
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break
        print("Computer move:")
        r,c = get_computer_move(board)
        board[r][c] = "O"
        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

if __name__ == "__main__":
    main()
