# BFS 문제

from collections import deque
n, m = map(int, input().split()) # n: 행, m: 열

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y): # x: 행, y: 열
    queue = deque()
    queue.append((x, y))
    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 범위를 벗어나는 경우에는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우에는 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단 거리 반환

print(bfs(0, 0))