def binary(arr, key, low, high):
    while low <= high:
        middle = (low + high) // 2

        if key == arr[middle]:
            return True
        elif key > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return False

n = int(input())
nArr = list(map(int, input().split()))
nArr.sort()
m = int(input())
mArr = list(map(int, input().split()))

for i in range(m):
    if binary(nArr, mArr[i], 0, n - 1):
        print(1)
    else:
        print(0)
