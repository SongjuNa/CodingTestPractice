# 시뮬레이션 문제
n = int(input())
plan = input().split()

x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1] #행
dy = [-1, 1, 0, 0] #열
move_types = ['L', 'R', 'U', 'D']

for p in plan:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            x, y = nx, ny
print(x, y)