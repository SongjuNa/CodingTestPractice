from collections import deque

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    # 상하좌우 패턴
    dx = [-1, 1, 0, 0] # 행 위아래
    dy = [0, 0, -1, 1] # 열 좌우
    
    # 큐 생성, 시작점(0, 0)
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 지도 밖으로 나가면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽(0) 만나면 패스
            if maps[nx][ny] == 0:
                continue
                
            # 길(1)이면
            if maps[nx][ny] == 1:
                # 걸음 수를 기록하고 큐에 넣음
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    # 값이 1보다 크면 도착, 1이면 실패            
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1