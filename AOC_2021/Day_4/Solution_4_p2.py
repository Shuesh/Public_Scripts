import re

def main():
    call_order, boards = Input_to_List('Day_4/Input_4.txt')
    marked_boards = [[[False for _ in range(len(boards[0][0]))] for _ in range(len(boards[0]))] for _ in range(len(boards))]
    winning_boards = [False for _ in range(len(boards))]
    final_board = None

    for number in call_order:
        if (False not in winning_boards):
            break
        final_number = number
        for index,board in enumerate(boards):
            if (not winning_boards[index]):
                marked_boards[index] = Update_Boards(board, marked_boards[index], number)
                winning_boards[index] = Win_Check(marked_boards[index])
                final_board = index
    total = Calculate(boards[final_board], marked_boards[final_board])
    print(total * int(final_number))

def Input_to_List(path):
    match_string = r"\d+"

    file = open(path, 'r')
    call_order = re.findall(match_string,file.readline())
    line = file.readline()
    end_board = False

    return_list = []
    matrix = []

    while True:
        next_line = file.readline()
        line = re.findall(match_string, next_line)

        if not next_line:
            return_list.append(matrix)
            break

        else:
            if(end_board):
                return_list.append(matrix)
                matrix = [line]
                end_board = False
            else:
                if(line == []):
                    end_board = True
                else:
                    matrix.append(line)

    return call_order, return_list


def Update_Boards(board, marked_board, number):
    for row_index,row in enumerate(board):
        for term_index,term in enumerate(row):
            if (term == number):
                marked_board[row_index][term_index] = True
                return marked_board
    return marked_board
    
def Win_Check(board):
    for row in board:
        if (False not in row):
            return True
    for column in range(len(board[0])):
        if (board[0][column] == True and board[1][column] == True and board[2][column] == True and board[3][column] == True and board[4][column] == True):
            return True
    return False

def Calculate(board, marked_board):
    total = 0
    for row_index,row in enumerate(board):
        for term_index, term in enumerate(row):
            if marked_board[row_index][term_index] == False:
                total += int(term)

    return total


if __name__ == '__main__':
    main()