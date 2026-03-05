# 큐 문제...
from collections import deque
n = int(input())
queue = deque()  # popleft() 쓸 거니까

for i in range(1, n+1):
    queue.append(i)  # 1부터 n까지 적힌 카드 큐에 저장
    
while len(queue) > 1:  # 카드 1장 남을 때까지 반복
    queue.popleft()  # 맨 위 카드 버리고
    queue.append(queue.popleft())  # 맨 위 카드 빼서 아래로 이동
    
print(queue[0])