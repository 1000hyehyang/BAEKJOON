t = int(input())
for j in range(t):
    r, s = input().split()
    r = int(r)
    result = ''
    for i in range(len(s)):
      result = result+s[i]*r
    print(result)
