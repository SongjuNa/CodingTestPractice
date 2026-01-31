def solution(num_list):
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 == 1:
            odd += str(num)
        elif num % 2 == 0:
            even += str(num)
    
    total = int(odd)+int(even)
    
    return total