def solution(myString):
    answer = [part for part in myString.split('x') if part]
    return sorted(answer)