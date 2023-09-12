# 일단, 문자별 다이얼 숫자를 지정해줍니다.
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
change = ['C', 'F', 'I', 'L', 'O', 'S', 'V']
dial = {}
n = 3

for i in alphabet:
    dial[i] = n
    if i in change:
        n += 1

word = input()
time = 0

for c in word:
    time += dial[c]

print(time)
