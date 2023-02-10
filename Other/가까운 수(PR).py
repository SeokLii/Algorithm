def solution(array, n):
    array.sort()
    dis = n
    dismin = array[0]
    for i in array:
        if abs(n-i) < dis:
            dis = abs(n-i)
            dismin = i
        elif abs(n-i) == dis:
            continue
        else:
            return dismin
    return dismin