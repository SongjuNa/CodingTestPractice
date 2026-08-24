def solution(n, lost, reserve):
    #체육복 빌려줄 수 있는 학생 수(여벌 있는 학생 중 도난 당한 학생 수 반영)
    real_reserve = set(reserve) - set(lost)    
    #체육복 없는 학생
    real_lost = set(lost) - set(reserve)
    
    for i in real_reserve:
        if i-1 in real_lost:
            real_lost.remove(i-1)
        elif i+1 in real_lost:
            real_lost.remove(i+1)
            
    return n - len(real_lost)
    