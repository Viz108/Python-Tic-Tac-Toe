from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    print("Enter your move:", end=" ")
    next_move = int(input())
    if next_move < 1 or next_move > 9:
        print("Invalid input")
        enter_move(board)
    elif ((next_move - 1 ) // 3, (next_move - 1) % 3) in make_list_of_free_fields(board):
        board[(next_move - 1) // 3][(next_move - 1) % 3] = "O"
    else:
        print("Square taken")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []

    for i in range(3):
        for j in range(3):
            if(board[i][j] != "O" and board[i][j] != "X"):
                free_fields.append((i,j))

    return free_fields
            

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    victory_flag = False
    
    #Horizontal
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            victory_flag = True

    #Vertical
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            victory_flag = True

    #Diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        victory_flag = True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        victory_flag = True

    return victory_flag

def draw_move(board):
    # The function draws the computer's move and updates the board.

    valid_move = False

    while not valid_move:
        next_move = randrange(8) + 1
        if ((next_move - 1 ) // 3, (next_move - 1) % 3) in make_list_of_free_fields(board):
            board[(next_move - 1) // 3][(next_move - 1) % 3] = "X"
            valid_move = True
        

board = [[1,2,3], [4,5,6], [7,8,9]]
continue_game = True

display_board(board)
while(continue_game):
    enter_move(board)
    display_board(board)
    if(victory_for(board, "O")):
       print("Player victory")
       continue_game = False
       break
    if make_list_of_free_fields(board) == []:
        print("Tie")
        continue_game = False
        break
       
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("Computer victory")
        continue_game = False
        break
    if make_list_of_free_fields(board) == []:
        print("Tie")
        continue_game = False
        break
