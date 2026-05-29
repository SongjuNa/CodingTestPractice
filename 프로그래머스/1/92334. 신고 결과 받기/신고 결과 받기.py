def solution(id_list, report, k):

    answer = [0] * len(id_list)
    user_idx = {user_id: idx for idx, user_id in enumerate(id_list)}
    
    report_dict = {user_id: set() for user_id in id_list} # set()으로 중복 제거
    

    for rep in report:
        from_user, to_user = rep.split() 
        report_dict[to_user].add(from_user)
        
    for to_user, reporters in report_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                idx = user_idx[reporter]
                answer[idx] += 1
                
    return answer