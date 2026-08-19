def solution(array):
    count = {}
    
    for n in array:
        count[n] = count.get(n, 0) +1
        
    max_freq = max(count.values())
    
    #items()사용해서 key, value 한 쌍으로 꺼내기
    modes = [n for n, freq in count.items() if freq == max_freq]
    
    # 최빈값이 여러 개면 -1, 하나면 그 숫자 반환
    return -1 if len(modes) > 1 else modes[0]
    