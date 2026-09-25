board = [' '] * 9


def display_board():
    for i in range(3):
        row = board[i * 3:i * 3 + 3]
        print("|".join(row))
        if i < 2:
            print("-" * 5)
    print()


def winner_check(player):
    winning_pos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in winning_pos:
        a, b, c = pos
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def board_full():
    return ' ' not in board


def computer_move():
    # 1. Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            if winner_check('O'):
                return

            board[i] = ' '

    # 2. Block the human
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'

            if winner_check('X'):
                board[i] = 'O'
                return

            board[i] = ' '

    # 3. Take the first available position
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return


print("TIC-TAC-TOE")
print("HUMAN - X, COMPUTER - O")
print()

display_board()

while True:

    # HUMAN MOVE
    try:
        p = int(input("Enter the box to fill (1-9): "))

        if p < 1 or p > 9:
            print("Enter a number between 1 and 9.")
            continue

        if board[p - 1] != ' ':
            print("Already occupied.")
            continue

        board[p - 1] = 'X'

    except ValueError:
        print("Enter a valid number.")
        continue

    display_board()

    # Check human win
    if winner_check('X'):
        print("HUMAN WINS! CONGRATS!")
        break

    # Check draw
    if board_full():
        print("DRAW!")
        break

    # COMPUTER MOVE
    print("COMPUTER MOVE")
    computer_move()
    display_board()

    # Check computer win
    if winner_check('O'):
        print("COMPUTER WINS!")
        break

    # Check draw
    if board_full():
        print("DRAW!")
        break