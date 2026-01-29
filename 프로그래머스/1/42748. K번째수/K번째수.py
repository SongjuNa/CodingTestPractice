# 정렬 기초 문제!

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        
        cut = array[i-1:j] # 잘라서
        cut.sort() # 정렬
        
        answer.append(cut[k-1])
        
    return answer