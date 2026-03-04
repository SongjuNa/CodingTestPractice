import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()  # (값, 인덱스) 저장
result = []

for i in range(N):
    # 1. 새 원소보다 큰 값은 덱 뒤에서 제거 (단조 오름차순 유지)
    while dq and dq[-1][0] > arr[i]:
        dq.pop()

    # 2. 새 원소 추가
    dq.append((arr[i], i))

    # 3. 윈도우 벗어난 원소 앞에서 제거
    if dq[0][1] <= i - L:
        dq.popleft()

    # 4. 덱의 맨 앞이 현재 최솟값
    result.append(dq[0][0])

print(*result)