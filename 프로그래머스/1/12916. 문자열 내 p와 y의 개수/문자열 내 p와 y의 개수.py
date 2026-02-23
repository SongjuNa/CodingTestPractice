def solution(s):
    new_str = s.lower()
    
    count_p = 0
    count_y = 0
    
    for c in new_str:
        if c == 'p':
            count_p += 1
        if c == 'y':
            count_y += 1
    if count_p == count_y:
        return True
    else:
        return False
            
    
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True