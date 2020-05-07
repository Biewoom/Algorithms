from collections import deque

def FindGroup(Matrix, DeleteElems):
    for r in range(1, len(Matrix)):
        for c in range(1, len(Matrix[0])):
            if Matrix[r][c]:
                curblock = Matrix[r][c][0]
                condition1 = Matrix[r-1][c-1] and Matrix[r-1][c-1][0] == curblock
                condition2 = Matrix[r-1][c] and Matrix[r-1][c][0] == curblock
                condition3 = Matrix[r][c-1] and Matrix[r][c-1][0] == curblock
                if condition1 and condition2 and condition3:
                    DeleteElems.add(Matrix[r-1][c-1][1])
                    DeleteElems.add(Matrix[r-1][c][1])
                    DeleteElems.add(Matrix[r][c-1][1])
                    DeleteElems.add(Matrix[r][c][1])

def StacksToMatrix(stackboard, Matrix):
    StackboardCopy = [stack.copy() for stack in stackboard]
    row = len(Matrix)
    for c in range(len(StackboardCopy)):
        i = 0
        while StackboardCopy[c]:
            Matrix[row - 1 - i][c] = StackboardCopy[c].popleft()
            i += 1
    return

def Solve(m, n, stackboard, DeleteElems)->int:
    Matrix = [([None]*n) for i in range(m)]
    StacksToMatrix(stackboard, Matrix)
    FindGroup(Matrix, DeleteElems)

def solution(m, n, board):
    # board -> list of Stack and index #
    StackBoard = [deque() for i in range(n)]
    for r in range(m):
        for c in range(n):
            StackBoard[c].appendleft((board[r][c], n*r+c) )
    #############################
    Change = 1; Removed = 0
    while Change:
        DeleteElems = set()
        Solve(m, n, StackBoard, DeleteElems)
        Change = 1 if len(DeleteElems) else 0
        Removed += len(DeleteElems)

        temp = [deque() for i in range(n)]
        for tempStack, Stack in zip(temp, StackBoard):
            while Stack:
                Elem = Stack.popleft()
                if Elem[1] not in DeleteElems:
                    tempStack.append(Elem)
        StackBoard = temp

    return Removed


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    lines = input().split(",")
    board = []
    for line in lines:
        board.append(line[1:-1])

    result = solution(m,n, board)
    print(result)
