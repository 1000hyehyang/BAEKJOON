n = int(input())

i = 1

lst = []

while i <= n:
    word = input()
    lst.append(word)

    i += 1

lst = sorted(lst, key = lambda x : (len(x), x)) 

arr = []

for j in range(len(lst)):
    if lst[j] not in arr:
        arr.append(lst[j])

for elem in arr:
    print(elem)
