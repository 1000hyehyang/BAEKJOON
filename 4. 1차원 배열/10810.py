lst = list(map(int, input().split(' ')))

lst_bucket = []
lst_way_k = []
for i in range(lst[0]):  # 리스트에 바구니의 개수를 추가해준다.
    lst_bucket.append(0)

for i in range(lst[1]):  # 바구니에 공을 넣을 횟수만큼 방법을 입력받는다.
    lst_way = list(map(int, input().split(' ')))
    way_i = lst_way[0] # i번 바구니부터
    way_j = lst_way[1] # j번 바구니까지
    way_k = lst_way[2] # k번 번호가 적혀져 있는 공을 하나씩 넣는다.
    for j in range(way_i, way_j+1):
        lst_way_k.append(way_k)
    lst_bucket[way_i-1:way_j] = lst_way_k
    lst_way_k = []

print(*lst_bucket)
