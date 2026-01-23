n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    print(*row)
