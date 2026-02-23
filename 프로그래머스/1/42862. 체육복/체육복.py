def solution(n, lost, reserve):
    # 차집합 사용
    # 진짜 빌려줄 수 있는 학생들
    real_reserve = set(reserve) - set(lost)
    
    # 체육복 아예 없는 학생들
    real_lost = set(lost) - set(reserve)
    
    for r in real_reserve:
        # 앞번호 체크
        if r - 1 in real_lost:
            real_lost.remove(r - 1) 
            
        # 뒷번호 체크
        elif r + 1 in real_lost:
            real_lost.remove(r + 1) 
            
    # 전체 학생 - 체육수업 참여 불가한 학생
    return n - len(real_lost)