word = input().upper() # upper는 대소문자 구분하지 않기 위해 모든 문자를 대문자로 변환, 어차피 대문자로 출력할 거니까
word_list = list(set(word)) # set 사용해 중복 제거 집합 만들기
cnt = []
 
for i in word_list:
    cnt.append(word.count(i))
 
 
max_count = max(cnt)
if cnt.count(max_count) > 1:
    print("?")
else:
    print(word_list[cnt.index(max_count)])