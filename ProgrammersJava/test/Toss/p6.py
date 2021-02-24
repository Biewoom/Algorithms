my_input = input().split(";")
my_table = []

for my in my_input:
    my_table.append(my.split(" "))

n = len(my_table)
m = len(my_table[0])

answer = 0

for i in range(n):
    for j in range(m):
        if my_table[i][j] == "1":
            answer += 4
            # upper
            if i > 0 and my_table[i-1][j] == "1":
                answer -= 1
            # lower
            if i < (n-1) and my_table[i+1][j] == "1":
                answer -= 1
            # right
            if j < (m - 1) and my_table[i][j+1] == "1":
                answer -= 1
            #left
            if j > 0 and my_table[i][j-1] == "1":
                answer -= 1

print(answer)