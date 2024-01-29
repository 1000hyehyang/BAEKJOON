import sys
sys.setrecursionlimit(10000)

dxs, dys = [0, 0, 1, -1, -1, -1, 1, 1], [1, -1, 0, 0, 1, -1, 1, -1]  # 동 서 남 북 대 각 선 들

def is_range(x, y):
    return 0 <= x < h and 0 <= y < w

def is_island(x, y):
    grid[x][y] = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and grid[nx][ny] == 1:
            is_island(nx, ny)

res = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    grid = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(h)
    ]

    result = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                result += 1
                is_island(i, j)
    res.append(result)

for elem in res:
    print(elem)