import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(brd):
    print()
    for row in range(5):
        if row % 2 == 0:
            print(f'  {brd[row // 2][0]} | {brd[row // 2][1]} | {brd[row // 2][2]}')
        else:
            print('  ---------')
    print()


def check_for_win(brd):
    # Check rows
    for i in range(3):
        if brd[i][0] == brd[i][1] == brd[i][2]:
            if brd[i][0] == 'O':
                return True, 'O'
            if brd[i][0] == 'X':
                return True, 'X'

    # Check columns
    for i in range(3):
        if brd[0][i] == brd[1][i] == brd[2][i]:
            if brd[0][i] == 'O':
                return True, 'O'
            if brd[0][i] == 'X':
                return True, 'X'

    # Check diagonals
    if brd[0][0] == brd[1][1] == brd[2][2] or brd[2][0] == brd[1][1] == brd[0][2]:
        if brd[1][1] == 'O':
            return True, 'O'
        if brd[1][1] == 'X':
            return True, 'X'

    # Check for draw
    draw = True
    for i in range(3):
        for j in range(3):
            if brd[i][j] == ' ':
                draw = False

    return False, draw


def update_board(brd, row, col, plyr):
    if brd[row][col] == ' ':
        brd[row][col] = plyr
        return True
    else:
        return False


def new_board():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


# Initialize board
board = new_board()

# Initialize player switch
player_switch = 0

# Game loop
while True:
    # Clear screen and print board
    clear_terminal()
    print_board(board)

    # Check for win conditions
    win_result = check_for_win(board)
    game_over = False
    if win_result[0]:
        print(f'{win_result[1]} wins!!!\n\n')
        game_over = True
    elif win_result[1]:
        print(f"This one's a draw!\n\n")
        game_over = True
    if game_over:
        play_again = input('Play again? ("y" for Yes, "n" for No): ')
        if play_again == 'y':
            board = new_board()
            continue
        break

    # Set player
    player = 'X' if player_switch == 0 else 'O'
    print(f"{player} Player's Turn\n")

    # Ask for user input
    valid_rows = ['t', 'm', 'b']
    row_input = ''
    while row_input not in valid_rows:
        row_input = input('Which row do you want to play? ("t" for Top, "m" for Middle, "b" for Bottom): ')
    row_input = valid_rows.index(row_input)

    valid_cols = ['l', 'm', 'r']
    col_input = ''
    while col_input not in valid_cols:
        col_input = input('Which column do you want to play? ("l" for Left, "m" for Middle, "r" for Right): ')
    col_input = valid_cols.index(col_input)

    # Update the board and switch players if the placement is valid
    if update_board(board, row_input, col_input, player):
        # Switch players
        player_switch = (player_switch + 1) % 2
