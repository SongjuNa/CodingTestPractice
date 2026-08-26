def solution(number, k):
    new_number = []

    for num in number:
        while new_number and (new_number[-1] < num) and k > 0:
            new_number.pop()
            k -= 1

        new_number.append(num)
    if k > 0:
        new_number = new_number[:-k]
    return ''.join(new_number)