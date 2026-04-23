def solution(s, n):
    result = ''
    for c in s:
        if c == ' ':
            result += ' '
        elif c.isupper():
            result += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            result += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return result