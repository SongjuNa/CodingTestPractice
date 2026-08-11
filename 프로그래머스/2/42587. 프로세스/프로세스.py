def solution(priorities, location):
    #queue 생성 with 위치번호 부여
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0 

    while True: 
        #맨 앞의 값 꺼내서 cur에 담으면
        cur = queue.pop(0)
        
        #현재 값보다 중요도 더 큰 거 있으면 queue에 추가
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            
        else:
            answer += 1
            
            #방금 실행 완료한 값이 location
            if cur[0] == location:
                return answer