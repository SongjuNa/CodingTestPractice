def solution(survey, choices):

    score_board = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        disagree, agree = survey[i][0], survey[i][1]  
        choice = choices[i]
        
        
        if choice < 4:
            score_board[disagree] += (4 - choice)
        elif choice > 4:
            score_board[agree] += (choice - 4)
            
    answer = ''
    
    if score_board['R'] >= score_board['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if score_board['C'] >= score_board['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if score_board['J'] >= score_board['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if score_board['A'] >= score_board['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer