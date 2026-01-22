#바구니 n개에 공 m번
n, m = map(int, input().split())
basket = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())

    for idx in range(i-1, j):
        basket[idx] = k
#언패킹으로 리스트 내부 요소 출력
print(*basket)