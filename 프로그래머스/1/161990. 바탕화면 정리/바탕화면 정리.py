def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):  # 행
        for j in range(len(wallpaper[i])):  # 열
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]