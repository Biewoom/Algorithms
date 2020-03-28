def maximum(b_list):
    a = [0]*len(b_list); x = [0]*len(b_list)
    a[0] = x[1] = b_list[0];

    for i in range(1, len(b_list)-1):
        a[i] = x[i] + b_list[i] #update a
        x[i+1] = max(x[i], a[i])
    a[len(b_list)-1] = x[len(b_list)-1] + b_list[len(b_list)-1]
    return a

if __name__ == '__main__':
    t = int(input())
    b_list = list( map(int, input().split()) )
    result = maximum(b_list)
    print(*result)
