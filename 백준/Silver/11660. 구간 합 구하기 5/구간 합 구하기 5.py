import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 표 입력받기 (인덱스 맞추기 위해 앞에 [0] 추가)
A = [[0] * (n + 1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    A.append(row)

# 2차원 합배열(D) 만들기
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 내 위 + 내 왼쪽 - 중복된 대각선 + 현재 값
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    print(result)