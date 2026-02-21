def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))  #리스트 수정하는 명령어들은 변수 설정하지 말 것 기억하기!
        return arr