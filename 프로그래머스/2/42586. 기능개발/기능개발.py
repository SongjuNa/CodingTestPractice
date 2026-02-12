def solution(progresses, speeds):
    days = [] #총 걸리는 날짜
    
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        
        if remain % s == 0:
            day = remain // s
        else:
            day = (remain // s) + 1
            
        days.append(day)

    
    answer = []
    max_day = days[0]
    count = 1       
    
    for i in range(1, len(days)):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = days[i]  
            count = 1 
            
    answer.append(count) 
    
    return answer