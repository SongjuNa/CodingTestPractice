def solution(numbers):
    sol = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in sol:
        for number in numbers:
            if i == number:
                result.remove(number)
    return sum(result)