def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        bubble = False
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                bubble = True
        
        if not bubble:
            break
    
    for i in range(n):
        print(lst[i])

n = int(input())
lst = [
    int(input())
    for _ in range(n)
]

bubbleSort(lst)
