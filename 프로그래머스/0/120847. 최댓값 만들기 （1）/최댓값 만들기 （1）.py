def solution(numbers):
    answer = max(numbers)
    numbers.remove(answer)
    answer *= max(numbers)

    return answer