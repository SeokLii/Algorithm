def solution(wallpaper):
    miny, maxy = len(wallpaper), 0
    minx, maxx = len(wallpaper[0]), 0

    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            if miny > i:
                miny = i
            if maxy < i + 1:
                maxy = i + 1

            for j in range(len(wallpaper[0])):
                if wallpaper[i][j] == '#':
                    if minx > j:
                        minx = j
                    if maxx < j + 1:
                        maxx = j + 1

    return [miny, minx, maxy, maxx]