s = list(input())
string = 'abcdefghijklmnopqrstuvwxyz'
lst = list(string)
result = []

for i in range(len(lst)):
    if s.count(lst[i])>0:
        result.append(s.index(lst[i]))
    else:
        result.append(-1)

print(" ".join(map(str, result)))
