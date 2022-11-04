x = int(input())
n = int(input())

total = 0
lst = []
for i in range(n):
    ab = list(map(int, input().split()))
    lst.append(ab)
    total = total + lst[i][0]*lst[i][1]

if total == x:
    print('Yes')
else:
    print('No')
