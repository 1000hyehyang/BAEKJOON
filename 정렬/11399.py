n = int(input())
arr = list(map(int, input().split()))
# 각 사람이 돈을 인출하는데 걸리는 시간 Pi
arr.sort()
l = len(arr)
result = 0
for i in range(l):
    result += arr[i] * l
    l -= 1
    
print(result)
