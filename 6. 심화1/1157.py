word = input().upper()

newWord = sorted(word)
dic = {}

for i in range(len(newWord)):
    if i < len(newWord) - 1:
        if newWord[i] != newWord[i + 1]:
            dic[newWord[i]] = newWord.count(newWord[i])
    else:
        dic[newWord[-1]] = newWord.count(newWord[-1])

newDic = list(dic.values())
newDic2 = list(dic.keys())

result = 0
answer = ''

for i in range(len(newDic)):
    if newDic[i] > result:
        result = newDic[i]
        answer = newDic2[i]
    elif newDic[i] == result:
        answer = '?'

print(answer)
