def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        ary = array[i-1:j]
        ary.sort()
        answer.append(ary[k-1])
        
    return answer