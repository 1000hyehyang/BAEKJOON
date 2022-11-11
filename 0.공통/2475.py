n = list(map(int, input().split()))
total = 0
for i in range(len(n)):
    x = n[i]*n[i]
    total = total + x

result = total%10
print(result)
