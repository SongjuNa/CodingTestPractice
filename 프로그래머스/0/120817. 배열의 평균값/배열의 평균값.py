def solution(numbers):
    total = 0
    for i in numbers:
        total += int(i)
    answer = total/len(numbers)
    return answer