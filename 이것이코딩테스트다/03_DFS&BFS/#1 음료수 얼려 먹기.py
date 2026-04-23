# DFS 문제

n, m = map(int, input().split()) # n: 행, m: 열

# 2차원 리스트 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y): # x: 행, y: 열
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 그래프 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0: # 현재 노드 방문하지 않았다면
        graph[x][y] = 1 # 방문 처리
        # 상, 하, 좌, 우 위치들도 모두 재귀적으로 호출
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

result = 0
for i in range(n):  # 모든 노드(위치)에 대하여 음료수 채우기
    for j in range(m):
        if dfs(i, j) == True: # 현재 위치에서 DFS 수행
            result += 1

print(result)