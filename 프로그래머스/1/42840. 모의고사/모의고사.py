# 완전탐색 기초 문제!

def solution(answers):
    # 각 수포자의 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자 점수 초기화
    score = [0, 0, 0]
    
    for i, ans in enumerate(answers): # 인덱스(문제 번호)랑 value(정답) 세트로 묶음(enumerate 사용)
        # 1번 수포자 채점
        if ans == p1[i % 5]: # 패턴 5개씩 반복
            score[0] += 1
        # 2번 수포자
        if ans == p2[i % 8]: # 패턴 8개씩 반복
            score[1] += 1
        # 3번 수포자
        if ans == p3[i % 10]: # 패턴 10개씩 반복
            score[2] += 1
    
    # 셋 중 가장 높은 점수
    max_score = max(score)
    
    # 제일 높은 점수 누군지 찾기
    result = []
    for i in range(3):
        if score[i] == max_score:
            result.append(i+1)
                   
    return result