n = int(input())
a = list(map(int, input().split()))

a.sort()
count = 0

for k in range(n):
    find = a[k]  # 찾고자 하는 값
    i = 0
    j = n-1  # 포인터 2개
    while i < j:
        if a[i] + a[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k: # 왼쪽 포인터가 나 자신이면 한 칸 옆으로
                i += 1
            elif j == k: # 오른쪽 포인터가 나 자신이면 한 칸 옆으로
                j -= 1  
          
        # 합이 타겟보다 작으면 숫자를 키워야 하니 왼쪽 이동
        elif a[i] + a[j] < find:
            i += 1
        # 합이 타겟보다 크면 숫자를 줄여야 하니 오른쪽 이동
        else:
            j -= 1

print(count)