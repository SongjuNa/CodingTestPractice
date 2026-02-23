import heapq

def solution(scoville, K):
    # 힙 생성
    heapq.heapify(scoville)
    count = 0
    
    # K보다 작다는 조건에서 계속 반복
    while scoville[0] < K:
        # 섞은 후 음식이 딱 1개 남았을 경우
        if len(scoville) == 1:
            return -1
        # 스코빌 지수 낮은 두 음식 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 두 음식 스코빌 지수 섞기
        new_food = first + (second*2)
        
        # new_food 다시 힙에 추가
        heapq.heappush(scoville, new_food)
        
        count += 1
        
    return count