import os
import sys
from collections import defaultdict, deque

def Delete(delete_set, board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in delete_set:
                board[r][c] = 0

def Check(board):
    delete_set = set()
    Map = defaultdict(list)
    c_stack = [deque() for i in range(len(board[0]))]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]:
                Map[board[r][c]].append( (r,c) )
                c_stack[c].appendleft(board[r][c])

    for num in Map:
        block_status, start_point = StatusCheck(Map[num])
        if ValidCheck(block_status, start_point, num, c_stack):
            delete_set.add(num)
    return delete_set

def ValidCheck(block_status, start_point, num, c_stack):

    if block_status in [6, 5, 4, 12, 13, 8, 9]: return False
    else:
        if block_status == 0:
            if c_stack[start_point[1]+1][-1] == c_stack[start_point[1]+2][-1] == num: return True
        elif block_status == 1:
            if c_stack[start_point[1]][-1] == c_stack[start_point[1]+2][-1] == num: return True
        elif block_status == 2:
            if c_stack[start_point[1]][-1] == c_stack[start_point[1]+1][-1] == num: return True
        elif block_status == 10:
            if c_stack[start_point[1]][-1] == num: return True
        elif block_status == 14:
            if c_stack[start_point[1]+1][-1] == num: return True
        else:
            print("other form?: Impossible")

    return False

def MakeStartPoint(form1, form2, llist):
    X = max([x[0] for x in llist])
    Y = min([x[1] for x in llist])
    return (X,Y)

def StatusCheck(llist):
    map_x = defaultdict(int)
    map_y = defaultdict(int)
    form1 = form2 = form3 = None

    for elem in llist:
        map_x[elem[0]] += 1; map_y[elem[1]] += 1

    max_x_times = max(map_x.values()); max_y_times = max(map_y.values())
    form1 = 0 if max_x_times > max_y_times else 1

    if form1:
        #vertical
        min_y_key = min(map_y.keys()); max_y_key = max(map_y.keys())
        form2 = 1 if map_y[min_y_key] == 3 else 0
        if form2:
            # right
            left_elems = [x[0] for x in llist if x[1] == min_y_key]
            right_elem = [x[0] for x in llist if x[1] == max_y_key][0]
            if right_elem == max(left_elems): form3 = 2
            elif right_elem == min(left_elems): form3 = 0
            else: form3 = 1
        else:
            # left
            left_elem = [x[0] for x in llist if x[1] == min_y_key][0]
            right_elems = [x[0] for x in llist if x[1] == max_y_key]
            if left_elem == max(right_elems): form3 = 2
            elif left_elem == min(right_elems): form3 = 0
            else: form3 = 1
    else:
        #horizontal
        min_x_key = min(map_x.keys()); max_x_key = max(map_x.keys())
        form2 = 1 if map_x[min_x_key] == 3 else 0
        if form2:
            # lower
            upper_elems = [x[1] for x in llist if x[0] == min_x_key]
            lower_elem = [x[1] for x in llist if x[0] == max_x_key][0]
            if lower_elem == max(upper_elems): form3 = 2
            elif lower_elem == min(upper_elems): form3 = 0
            else: form3 = 1
        else:
            # upper
            upper_elem = [x[1] for x in llist if x[0] == min_x_key][0]
            lower_elems = [x[1] for x in llist if x[0] == max_x_key]
            if upper_elem == max(lower_elems): form3 = 2
            elif upper_elem == min(lower_elems): form3 = 0
            else: form3 = 1


    status = 0
    status |= form1 << 3
    status |= form2 << 2
    status |= form3

    start_point = MakeStartPoint(form1, form2, llist)
    return status, start_point

def Solve(board):
    delete_set = Check(board)
    if delete_set:
        Delete(delete_set, board)
        return (len(delete_set) + Solve(board) )
    else: return 0

def solution(board):
    answer = Solve(board)
    return answer

if __name__ == '__main__':
    board = []
    lines = input()[1:-1].split("],[")

    for line in lines:
        int_line = list(map(int, line.split(",")))
        board.append(int_line)
    print(solution(board))
