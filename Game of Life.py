import random
import matplotlib.pyplot as plt
import time



def render(board):
    plt.imshow(board, cmap='Greys', interpolation='nearest')
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()
    # print()
    # row = len(board)
    # col = len(board[0])
    # i = 0
    # j = 0
    # for i in range(row):
    #     print("|",end=" ")
    #     for j in range(col):
    #         print("O" if board[i][j] == 1 else ".", end=" ")
    #     print("|")


def dead_state(width, height):
    board = []
    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(0)
    return board

def random_state(width, height):
    state = dead_state(width,height)
    i = 0
    for i in range(0, height):
        for j in range(0, width):
            state[i][j] = random.randint(0, 1)
    return state

def corner_case(board, x, y):
    score = 0
    row = len(board)
    col = len(board[0])
    if x == 0 and y == 0:
        if board[x][y+1] == 1:
            score +=1
        if board[x+1][y] == 1:
            score += 1
        if board[x+1][y+1] == 1:
            score += 1
        if board[-1][y] == 1:
            score += 1
        if board[-1][y+1] == 1:
            score += 1
        if board[-1][-1] == 1:
            score += 1
        if board[x][-1] == 1:
            score += 1
        if board[x+1][-1] == 1:
            score += 1
        return score
    if x == 0 and y == col-1:
        if board[x-1][y] == 1:
            score += 1
        if board[x-1][y-1] == 1:
            score += 1
        if board[x-1][y] == 1:
            score += 1
        if board[-1][y] == 1:
            score += 1
        if board[-1][0] == 1:
            score += 1
        if board[-1][y-1] == 1:
            score += 1
        if board[0][0] == 1:
            score += 1
        if board[1][0] == 1:
            score += 1
        return score
    if x == row-1 and y == 0:
        if board [x-1][y] == 1:
            score +=1
        if board[x-1][y+1] == 1:
            score +=1
        if board[x][y+1] == 1:
            score += 1
        if board[x][-1] == 1:
            score += 1
        if board[x - 1][-1] == 1:
            score += 1
        if board[0][0] == 1:
            score += 1
        if board[0][1] == 1:
            score += 1
        if board[0][-1] == 1:
            score += 1
        return score
    if x == row-1 and y == col-1:
        if board[x-1][y] == 1:
            score += 1
        if board[x-1][y-1] == 1:
            score += 1
        if board [x][y-1] == 1:
            score+=1
        if board[x][0] == 1:
            score += 1
        if board[x-1][0] == 1:
            score +=1
        if board[0][y] == 1:
            score +=1
        if board[0][y-1] == 1:
            score += 1
        if board[0][0] == 1:
            score += 1
        return score

def edge_case(board, x, y):
    score = 0
    row = len(board)
    col = len(board[0])
    score = 0
    if x == 0:
        if board[x][y-1] == 1:
            score += 1
        if board[x][y+1] == 1:
            score +=1
        if board[x+1][y] == 1 :
            score +=1
        if board[x+1][y+1]==1:
            score +=1
        if board[x+1][y-1] == 1:
            score +=1
        if board[-1][y] == 1:
            score +=1
        if board[-1][y-1] == 1:
             score +=1
        if board[-1][y+1] == 1:
            score +=1
        return score
    if x == row -1:
        if board[x][y-1] == 1:
            score += 1
        if board[x][y+1] == 1:score +=1
        if board[x-1][y] == 1: score +=1
        if board[x-1][y-1] == 1  : score +=1
        if board[x-1][y+1]== 1 : score +=1
        if board[0][y] == 1: score +=1
        if board[0][y-1] ==1  : score +=1
        if board[0][y+1]==1 : score +=1
        return score
    if y == 0 :
        if board[x-1][y] == 1 : score +=1
        if board[x+1][y] == 1 : score +=1
        if board[x][y+1] == 1 : score +=1
        if board[x+1][y+1] == 1 : score +=1
        if board[x-1][y+1] == 1 : score +=1
        if board[x][-1] == 1 : score +=1
        if board[x+1][-1] == 1 : score +=1
        if board[x-1][-1] == 1 : score +=1
        return score
    if y == col -1:
        if board[x-1][y] == 1 : score +=1
        if board[x+1][y] == 1 : score +=1
        if board[x][y-1] ==1 : score +=1
        if board[x-1][y-1] == 1 : score +=1
        if board[x+1][y-1] ==1 :score +=1
        if board[x][0] == 1 : score +=1
        if board[x-1][0] == 1 :score +=1
        if board[x+1][0] == 1 : score +=1
        return score
    return score

def normal_case(board,x,y):
    score = 0
    row = len(board)
    col = len(board[0])
    if board[x + 1][y] == 1:
        score += 1
    if board[x - 1][y] == 1:
        score += 1
    if board[x][y + 1] == 1:
        score += 1
    if board[x][y - 1] == 1:
        score += 1
    if board[x + 1][y + 1] == 1:
        score += 1
    if board[x + 1][y - 1] == 1:
        score += 1
    if board[x - 1][y - 1] == 1:
        score += 1
    if board[x - 1][y + 1] == 1:
        score += 1
    return score

def check_bounds(board,x,y):
    row = len(board)
    col = len(board[0])
    if (x == 0 and y == 0) or (x == 0 and y == col - 1) or (x == row -1  and y == 0) or (x == row -1 and y == col -1):
        return corner_case(board,x,y)
    elif (x == 0 or x == row-1) or (y ==0 or y == col -1):
        return edge_case(board,x,y)
    else:
        return normal_case(board,x,y)

def next_state(current):
    row = len(current)
    col = len(current[0])
    next_board = dead_state(row,col)
    for x in range(0, row):
        for y in range(0, col):
            score = check_bounds(current,x,y)
            if current[x][y] == 1 and (score == 2 or score == 3):
                next_board[x][y] = 1
            elif current[x][y] == 0 and (score == 3):
                next_board[x][y] = 1
            else :
                next_board[x][y] = 0
    return next_board

def load_txt_file(filename):
    board = []
    with open(filename, 'r') as file:
         for line in file:
             line = line.strip()
             row = [int(char) for char in line]
             board.append(row)
    file.close()
    return board


if __name__ == '__main__':
    # start = random_state( 25,25)
    # board = start
    # for _ in range(30):
    #     render(board)
    #     board = next_state(board)


    start = load_txt_file('toad.txt')
    board = start
    for _ in range(15):
        render(board)
        board = next_state(board)




