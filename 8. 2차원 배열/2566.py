arr = [
    list(map(int, input().split()))
    for _ in range(9)
]
maxi = 0
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxi:
            maxi = arr[i][j]
            a, b = i, j

print(maxi)
print(a + 1, b + 1)
