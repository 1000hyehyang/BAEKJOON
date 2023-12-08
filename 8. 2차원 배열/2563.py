n = int(input())

arr = [
    [0] * 101
    for _ in range(101)
]

for i in range(n):
    a, b = tuple(map(int, input().split()))
    for j in range(10):
        for k in range(10):
            arr[a + k][b + j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            result += 1

print(result)
