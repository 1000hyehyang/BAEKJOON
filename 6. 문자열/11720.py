n = int(input())
total = 0

lst = list(map(int, input()))

for i in range(n):
    total = total + lst[i]

print(total)
