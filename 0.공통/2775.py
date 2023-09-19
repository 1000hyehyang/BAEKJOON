T = int(input())

for i in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    lst = [
        i 
        for i in range(1, n + 1) # 0층
    ]

    for _ in range(k):  
        for j in range(1, n):
            lst[j] += lst[j - 1]
    print(lst[n - 1])
