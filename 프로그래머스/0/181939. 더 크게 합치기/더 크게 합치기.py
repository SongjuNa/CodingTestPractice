def solution(a, b):
    num1 = str(a)+str(b)
    num2 = str(b)+str(a)
    
    if int(num1) > int(num2):
        return int(num1)
    elif int(num1) < int(num2):
        return int(num2)
    else:
        return int(num1)