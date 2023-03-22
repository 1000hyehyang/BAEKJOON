lst = list(map(int, input().split(' ')))

lst_bucket = []

for i in range(lst[0]):  # 리스트에 바구니의 개수만큼 번호에 맞는 공 하나를 추가해준다.
    lst_bucket.append(i+1)

for i in range(lst[1]):  # 바구니에 공을 넣을 횟수만큼 방법을 입력받는다.
    lst_way = list(map(int, input().split(' ')))
    way_i = lst_way[0] # i번 바구니
    way_j = lst_way[1] # j번 바구니
    lst_bucket[way_i-1:way_j] = reversed(lst_bucket[way_i-1:way_j]) # reversed() 메소드는 인자로 받은 iterable 객체 요소들을 역순으로 반환한다.

print(*lst_bucket)
