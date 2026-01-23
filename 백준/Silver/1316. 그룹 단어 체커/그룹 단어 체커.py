n = int(input())

for _ in range(n):
    word = input()
    
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):  # find 함수는 그 문자가 문자열에서 처음 등장하는 위치(인덱스) 알려줌
            n -= 1
            break
print(n)
        