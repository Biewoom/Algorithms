from collections import deque

def print_banks(Q):
    for i, q in zip(range(0, 5), Q):
        print(" ".join(Q) )
    else:
        print(" ".join(Q[:5]))
    
my_input = input()
my_list = my_input.split(" ")

my_set = set()
my_queue = deque()

for bank in my_list:
    if bank in my_set:
        my_queue.remove(bank)
    my_set.add(bank)
    my_queue.appendleft(bank)
    print_banks(my_queue)