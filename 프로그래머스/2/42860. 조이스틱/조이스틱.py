def solution(name):
    # 위아래 조작
    answer = sum(min(ord(i) - ord('A'), 26 - (ord(i) - ord('A'))) for i in name)
    
    # 좌우 조작
    move = len(name) - 1
    
    for i in range(len(name)):
        j = i + 1
        # 연속된 A 구간 찾기
        while j < len(name) and name[j] == 'A':
            j += 1
        # 오른쪽으로 갔다가 왼쪽으로 돌아오는 경우
        move = min(move, i + len(name) - j + min(i, len(name) - j))
    
    return answer + move