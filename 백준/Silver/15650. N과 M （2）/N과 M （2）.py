n, m = tuple(map(int, input().split()))
selected = []

def print_answer():
    for elem in selected:
        print(elem, end = ' ')
    print()

def choose(cur_num, cnt):
    if cur_num == n + 1:
        if cnt == m:
            print_answer()
        return
    
    selected.append(cur_num)
    choose(cur_num + 1, cnt + 1)
    selected.pop()

    choose(cur_num + 1, cnt)
    

choose(1, 0)