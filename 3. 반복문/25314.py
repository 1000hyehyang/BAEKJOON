n = int(input())
count = int(n/4)

result = 'int'

for i in range(count):
    result = 'long' + ' ' + result

print(result)
