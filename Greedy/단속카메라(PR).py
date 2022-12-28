def solution(routes):
    # [[-20,-15], [-18,-13], [-14,-5], [-5,-3]]
    # routes[i][1] > routes[i+1][0]

    routes.sort(key=lambda x: x[1])
    answer = 1
    check = routes[0][1]
    for i in range(1, len(routes)):
        if check < routes[i][0]:
            print(check, routes[i][0])
            answer += 1
            check = routes[i][1]

    return answer

