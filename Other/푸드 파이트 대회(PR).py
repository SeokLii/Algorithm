def solution(food):
    foods = ''
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            foods += str(i) * ((food[i] - 1) // 2)
        else:
            foods += str(i) * (food[i] // 2)

    return foods + '0' + foods[::-1]