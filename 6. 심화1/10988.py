word = input()
length = len(word)

result = 1

for i in range(length // 2):
    if word[i] != word[length - i - 1]:
        result = 0
        break

print(result)
