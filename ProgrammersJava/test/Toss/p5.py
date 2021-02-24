kim_toss = [int(x) for x in input().split(" ")]
yee_toss = [int(x) for x in input().split(" ")]

out_toss = []
left_x = 0
left_y = 0

for x, y in zip(kim_toss, yee_toss):
    if (x+ left_x) > (y + left_y):
        out_toss.append( (x+left_x) - (y+left_y) )
        left_x = left_y = 0
    else:
        out_toss.append(0)
        left_x += x
        left_y += y

print(" ".join([str(x) for x in out_toss]))