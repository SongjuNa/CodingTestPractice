import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(map(int, input().split()))

s.sort()  # 투 포인터를 쓰려면 정렬이 필수 조건

count = 0
i = 0
j = n-1
while i < j:
    sum = s[i] + s[j]
    
    if sum == m:
        count += 1
        i += 1
        j -= 1  # 포인터 2개 각각 안쪽으로 이동
    elif sum < m:
        i += 1  # 시작 포인터 오른쪽으로 이동
    else:
        j -= 1  # 마지막 포인터 왼쪽으로 이동
print(count)