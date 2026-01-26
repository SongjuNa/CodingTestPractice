def solution(participant, completion):
    count = {}

    for p in participant:
        count[p] = count.get(p, 0) + 1

    for c in completion:
        count[c] -= 1

    for name in count:
        if count[name] == 1:
            return name