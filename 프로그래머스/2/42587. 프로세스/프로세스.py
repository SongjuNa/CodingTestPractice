def solution(priorities, location):
    #대기열(queue) 생성 (위치번호 부여)
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0 

    while True: 
        # 맨 앞 꺼내기
        cur = queue.pop(0)
        
        # 현재 값보다 중요도 더 큰 거 있으면 queue에 추가
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            
        else:
            answer += 1
            
            # 방금 인쇄한 값이 location
            if cur[0] == location:
                return answer