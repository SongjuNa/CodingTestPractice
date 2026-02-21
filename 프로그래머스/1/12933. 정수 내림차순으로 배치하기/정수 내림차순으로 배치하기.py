# sort()는 리스트만 사용 가능 (리스트.sort())
# sorted()는 파이썬 자체 내장함수, 모든 데이터 사용 가능 (변수명=sorted(데이터))

def solution(n):
    new_list = list(str(n))
    new_list.sort(reverse=True)
    answer = int("".join(new_list)) #join함수 = 접착제 역할(여기선 ""를 기준으로)
    return answer