def solution(people, limit):
    people.sort()
    lightest = 0
    heaviest = len(people) - 1
    count = 0

    while lightest <= heaviest:
        if people[lightest] + people[heaviest] <= limit:
            lightest += 1 

        heaviest -= 1 
        count += 1

    return count