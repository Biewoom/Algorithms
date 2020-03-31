import os
import sys




def Checker(value) -> list:
    #result = [pillar's start, pillar's end, bar's start, bar's end]
    _bit = '{:04b}'.format(value)
    result = []

    for _ in _bit:
        if _ == '0': result.append(False)
        elif _ == '1': result.append(True)
        else: print("Impossible: ", _)
    return result

def CoordSwapper1(coord, matrix): # problemSetting coord -> build_it coord
    x, y = coord
    swapped_x = len(matrix) - 1 - y
    swapped_y = x
    return (swapped_x, swapped_y)

def CoordSwapper2(coord, matrix): # built_in coord -> problemSetting coord
    x, y = coord
    swapped_x = y
    swapped_y = len(matrix) - 1 - x
    return (swapped_x, swapped_y)

def pillar_alive(coord, matrix):
    x, y = coord
    pillar_start, pillar_end, bar_start, bar_end = Checker(matrix[x][y])

    if pillar_end or bar_start or bar_end: return True
    else: return False

def bar_alive(coord, matrix, ttype):
    x, y = coord

    C_pillar_start, C_pillar_end, C_bar_start, C_bar_end = Checker(matrix[x][y])

    if ttype == 'left':
        L_pillar_start, L_pillar_end, L_bar_start, L_bar_end = Checker(matrix[x][y-1])
        if C_pillar_end or L_pillar_end: return True
        elif C_bar_start and L_bar_end: return True
        else: return False

    elif ttype == 'right': # given is start
        R_pillar_start, R_pillar_end, R_bar_start, R_bar_end = Checker(matrix[x][y+1])
        if C_pillar_start or R_pillar_end: return True
        elif C_bar_end and R_bar_start: return True
        else: return False
    else:
        print('IMPOSSIBLE')


def remove_bar(coord, matrix):
    x, y = coord
    L_pillar_start, L_pillar_end, L_bar_start, L_bar_end = Checker(matrix[x][y])
    R_pillar_start, R_pillar_end, R_bar_start, R_bar_end = Checker(matrix[x][y+1])

    if not L_pillar_start: return
    #remove
    matrix[x][y]^= 2; matrix[x][y+1]^= 1

    L_pillar_TEST = True if (not L_pillar_start) or pillar_alive((x,y), matrix) else False
    R_pillar_TEST = True if (not R_pillar_start) or pillar_alive((x, y+1), matrix) else False
    L_bar_TEST = True if (not L_bar_end) or bar_alive((x, y), matrix, 'left') else False
    R_bar_TEST = True if (not R_bar_start) or bar_alive((x, y+1), matrix, 'right') else False

    if L_pillar_TEST and R_pillar_TEST and L_bar_TEST and R_bar_TEST: return
    else: matrix[x][y]|= 2; matrix[x][y+1]|= 1 #reinstall


def remove_pillar(coord, matrix):
    x, y = coord
    D_pillar_start, D_pillar_end, D_bar_start, D_bar_end = Checker(matrix[x][y])
    U_pillar_start, U_pillar_end, U_bar_start, U_bar_end = Checker(matrix[x-1][y])

    if not D_pillar_start: return
    #remove
    matrix[x][y]^= 8; matrix[x-1][y]^= 4

    U_pillar_TEST = True if (not U_pillar_start) or pillar_alive((x-1, y), matrix) else False
    L_bar_TEST = True if (not U_bar_end) or bar_alive((x-1, y), matrix, 'left') else False
    R_bar_TEST = True if (not U_bar_start) or bar_alive((x-1, y), matrix, 'right') else False

    if U_pillar_TEST and L_bar_TEST and R_bar_TEST: return
    else: matrix[x][y]|= 8; matrix[x-1][y]|= 4 # reinstall


def install_pillar(coord, matrix):
    x, y = coord
    pillar_start, pillar_end, bar_start, bar_end = Checker(matrix[x][y])

    if x == len(matrix)-1 or bar_start or bar_end or pillar_end:
        matrix[x][y] |= 8
        matrix[x-1][y] |= 4

def install_bar(coord, matrix):
    x, y = coord
    L_pillar_start, L_pillar_end, L_bar_start, L_bar_end = Checker(matrix[x][y])
    R_pillar_start, R_pillar_end, R_bar_start, R_bar_end = Checker(matrix[x][y+1])

    if L_pillar_end or R_pillar_end or (L_bar_end and R_bar_start):
        matrix[x][y] |= 2
        matrix[x][y+1] |= 1

def show_all(matrix, res):
    n = len(matrix)

    for x in range(n):
        for y in range(n):
            pillar_start, pillar_end, bar_start, bar_end = Checker(matrix[x][y])
            _x, _y = CoordSwapper2( (x, y), matrix)
            if pillar_start: res.append([_x,_y,0])
            if bar_start: res.append([_x,_y,1])
    return

def solution(n, build_frame):

    res = []; matrix = [[0]*(n+1) for i in range(n+1)]
    # bit manipulation:
    # 0000: Nothing, 1000: pillar_start, 1100: pillar's start and end
    # 0010: bar's start_point, 0001: bar's end_point
    # 00|00 -> the first two digits represent pillar, the other represent bars

    for op in build_frame:
        x, y, a, b = op

        _x, _y = CoordSwapper1((x,y), matrix)
        if a == 0 and b == 0: remove_pillar((_x,_y), matrix)
        elif a == 0 and b == 1: install_pillar((_x,_y), matrix)
        elif a == 1 and b == 0: remove_bar((_x,_y), matrix)
        elif a == 1 and b == 1: install_bar((_x,_y), matrix)
        else: print("IMPOSSIBLE: ", op)

    show_all(matrix, res)
    res.sort()

    return res


if __name__ == '__main__':
    n = int(input())
    build_frame = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        build_frame.append(list(map(int, line.split())))
    result = solution(n, build_frame)
    print(result)
