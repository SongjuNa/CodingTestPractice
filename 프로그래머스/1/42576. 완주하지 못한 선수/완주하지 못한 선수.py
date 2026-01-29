# 해시 기초 문제!

def solution(participant, completion):
    count = {} # 딕셔너리

    for p in participant:
        count[p] = count.get(p, 0) + 1  # count에서 p 있으면 가져오고, 없으면 0(그리고 1(명)) 추가)

    for c in completion: # count에서 완주자 삭제하기
        count[c] -= 1

    for name in count:
        if count[name] == 1:
            return name