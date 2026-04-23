# 시뮬레이션 문제
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        
        # 오, 아, 왼, 위
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x, y, dir = 0, 0, 0
        
        for _ in range(len(matrix) * len(matrix[0])):
            result.append(matrix[x][y])
            visited[x][y] = True
            
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            # 벽이거나 이미 방문했으면 방향 전환
            if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]) or visited[nx][ny]:
                dir = (dir + 1) % 4
                nx = x + dx[dir]
                ny = y + dy[dir]
            
            x, y = nx, ny
        
        return result
