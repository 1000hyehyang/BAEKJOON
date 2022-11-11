a, b = map(int, input().split())
result1 = a
result2 = b

while a!=0 or b!=0 :
    temp1 = a%10
    temp2 = b%10
    a = a/10
    b = b/10
    if temp1>temp2:
        x = (result1%10)*100+((result1//10)%10)*10+result1//100
        print(x)
        break
    if temp2>temp1:
        y = (result2%10)*100+((result2//10)%10)*10+result2//100
        print(y)
        break
