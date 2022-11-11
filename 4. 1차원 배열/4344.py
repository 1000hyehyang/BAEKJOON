c = int(input())
lst = []
total = 0
for i in range(c):
    n = list(map(int, input().split()))
    for j in range(n[0]):
        total = total + n[j+1]

    m = total/(n[0])

    for k in range(n[0]):
        if n[k+1]>m :
            lst.append(n[k+1])
    result = len(lst)
    x = result/n[0]*100
    total = 0
    lst = []
    print('%.3f%%' %x)
