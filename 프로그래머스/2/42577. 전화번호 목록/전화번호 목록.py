def solution(phone_book):
    
    numbers = set(phone_book)

    for n in phone_book:
        for i in range(1, len(n)):
            if n[:i] in numbers:
                return False
    return True
    
    
    
    
    
    
    
    return answer