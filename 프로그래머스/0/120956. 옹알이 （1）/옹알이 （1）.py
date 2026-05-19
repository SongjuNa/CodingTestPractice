def solution(babbling):
    pronounce = {1: "aya", 2: "ye", 3: "woo", 4: "ma"}
    
    result = 0
    for word in babbling:
        for p in pronounce.values():
            if p in word:
                word = word.replace(p, " ")
                
        if word.replace(" ", "") == "":
            result += 1       
        
    return result