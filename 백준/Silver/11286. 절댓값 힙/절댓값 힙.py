# 우선순위 큐(힙)
import sys, heapq
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x != 0:  # x가 0이 아니라면
        heapq.heappush(heap, (abs(x), x))  # 힙에 절댓값의 최솟값 넣음(튜플로 저장) -> 절댓값 기준으로 먼저 줄 세우고, 같으면 진짜 데이터의 최솟값으로 정렬
    else: # x가 0이라면
        if heap:  # 힙이 비어있지 않을 때
            print(heapq.heappop(heap)[1])   # 절댓값이 가장 작은 값 자체를 출력하고 힙에서 제거
        else: # 힙이 비어있으면
            print(0)