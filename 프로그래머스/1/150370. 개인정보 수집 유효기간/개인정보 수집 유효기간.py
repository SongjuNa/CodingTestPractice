def calculate(date, r) :
    date = list(map(int, date.split('.')))
    return (date[0] * 12 + date[1]) * 28 + date[2] + r * 28



def solution(today, terms, privacies):
    split_terms = [i.split() for i in terms]
    answer = []
    for i in range(len(privacies)) :
        period, priv = privacies[i].split()
        j = 0
        while j < len(split_terms) :
            if split_terms[j][0] == priv : break
            j += 1
        if calculate(today, 0) >= calculate(period, int(split_terms[j][1])) : answer.append(i + 1)
    return answer