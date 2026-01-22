remainder = []

for _ in range(10):
    n = int(input())
    remainder.append(n%42) #나머지 빈 배열에 나머지 계산해서 추가

print(len(set(remainder)))  #나머지 리스트 중복 제거 후 길이 출력      