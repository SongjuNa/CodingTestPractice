while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    # 0 0 도 출력되지 않도록 순서 주의    
    print(a+b)