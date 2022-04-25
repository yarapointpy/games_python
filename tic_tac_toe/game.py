import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = 'X'
game_running = True
winner = None


def print_board():
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("-------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("-------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])


def user_guess(board):
    valid = True
    while valid:

        x = int(input('Enter a position (1-9): '))
        if 1 <= x <= 9 and board[x - 1] == '-':
            board[x - 1] = current_player
            valid = False

        else:
            print('This value is invalid!')
            print_board()


def computer_guess(board):
    while current_player == 'O':
        x = random.randint(1, 8)

        if board[x] == '-':
            board[x] = current_player
            switch_player()


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def check_tie():
    global game_running
    if '-' not in board:
        print('Is a tie!')
        print_board()
        game_running = False


def check_winner():
    global game_running

    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f'The winner is {winner}')
        print_board()
        game_running = False


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'

    else:
        current_player = 'X'


print("Welcome to tic-tac-toe!")
while game_running:

    print_board()

    user_guess(board)
    check_winner()
    check_tie()

    if game_running:

        switch_player()
        computer_guess(board)
        check_winner()

