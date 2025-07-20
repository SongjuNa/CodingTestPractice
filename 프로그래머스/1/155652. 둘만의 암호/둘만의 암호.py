def solution(s, skip, index):
    a = 'abcdefghijklmnopqrstuvwxyz'
    ls = ''
    for i in skip:
        a = a.replace(i,'')
    for j in s :
        if (a.index(j) + index) / len(a) >= 1:
            n = a.index(j) + index - len(a)*int((a.index(j) + index) / len(a))
            ls += a[n]
        else :
            n = a.index(j) + index
            ls += a[n]
    return ls