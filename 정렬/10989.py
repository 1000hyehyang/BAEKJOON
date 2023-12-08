from sys import stdin

lst = [0] * 10001

for _ in range(int(stdin.readline())):
    lst[int(stdin.readline())] += 1

for i in range(10001):
    for _ in range(lst[i]):
        print(i)
