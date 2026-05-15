def solution(today, terms, privacies):
    answer = []
    
    # 오늘 날짜를 총 일수로 변환
    y, m, d = today.split(".")
    today_days = (int(y) * 12 * 28) + (int(m) * 28) + int(d)
    
    # terms 배열을 딕셔너리로 변환(해시)
    term_dict = {}
    for term in terms:
        name, month = term.split(" ")
        term_dict[name] = int(month)
         
    # privacies 배열
    for i, p in enumerate(privacies):
        date, term_type = p.split(" ") 
        p_y, p_m, p_d = date.split(".")
        
        # 개인정보 수집 일자를 총 일수로 변환
        join_days = (int(p_y) * 12 * 28) + (int(p_m) * 28) + int(p_d)
        
        # 만료일 총 일수 계산
        expire_days = join_days + (term_dict[term_type] * 28)
        
        # 오늘 총 일수가 만료일보다 크거나 같으면 파기
        if today_days >= expire_days:
            answer.append(i + 1)

    return answer