lst = []
for i in range(1, 31):
    lst.append(i)

for i in range(28):
    n = int(input())
    lst.remove(n)

lst.sort()
print(lst[0])
print(lst[-1])
