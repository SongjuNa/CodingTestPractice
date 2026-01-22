#n개 바구니, m번 역순으로 바꾸기
n, m = map(int, input().split())
basket = list(range(1, n+1))

for _ in range(m):
    i, j  = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1] #i부터 j번 바구니까지 역순으로 바꾼 것 바구니 리스트에 업데이트
    
print(*basket)