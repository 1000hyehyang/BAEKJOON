n, m = tuple(map(int, input().split()))
selected = []

def print_answer():
    for elem in selected:
        print(elem, end = ' ')
    print()

def choose(cnt):
    if cnt == m:
        print_answer()
        return
    
    for i in range(1, n + 1):
        if i in selected:
            continue

        selected.append(i)
        choose(cnt + 1)
        selected.pop()

choose(0)