def solution(wallpaper):
    x_min = y_min = float('inf')
    x_max = y_max = 0
    for x, row in enumerate(wallpaper):
        for y, each in enumerate(row):
            if each == '#':
                x_min = min(x, x_min)
                x_max = max(x, x_max)
                y_min = min(y, y_min)
                y_max = max(y, y_max)
    return [x_min, y_min, x_max + 1, y_max + 1]