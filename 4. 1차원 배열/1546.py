n = int(input())
score = list(map(int, input().split(' ', n-1)))
score.sort()
m = score[-1]

lst = []
for i in range(n):
    x = score[i]/m*100
    lst.append(x)
total = 0
for i in range(n):
    total = total + lst[i]

print(total/n)
