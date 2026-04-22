# 시뮬레이션 문제-방향+이동

n, m = map(int, input().split())

# 방문한 위치 저장용 (n*m 맵을 0으로 초기화)
d = [[0] * m for _ in range(n)]

x, y, dir = map(int, input().split()) # 현재 위치, 방향
d[x][y] = 1 # 현재 좌표 방문 표시

# 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1 # 시작 위치 포함
turn_time = 0 # 회전한 횟수
while True:
    # 왼쪽으로 회전
    turn_left()
    # 회전한 이후 이동하려는 위치 (아직 이동은 안함)
    nx = x + dx[dir] 
    ny = y + dy[dir]
    #이제부터 이동
    # 회전한 이후 정면에 가보지 않은 칸 존재하면서 해당 칸이 육지인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny # 해당 칸으로 이동
        d[nx][ny] = 1 # 방문한 위치로 표시
        count += 1
        turn_time = 0 # 회전한 횟수 초기화
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)