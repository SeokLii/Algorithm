def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        check = 0
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            check += 1
            for _ in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    check += 1
                else:
                    break
            answer.append(check)
        else:
            for i in range(len(speeds)):
                progresses[i] += speeds[i]

    return answer