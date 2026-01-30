def solution(participant, completion):
    incompletion = {}
    
    for p in participant:
        incompletion[p] = incompletion.get(p, 0) +1
    for c in completion:
        incompletion[c] -= 1
    
    for name in incompletion:
        if incompletion[name] == 1:
            return name
    