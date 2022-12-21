def calculate(H, M, S):
    return H * 3600 + M * 60 + S


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    # 1. logs 파싱
    logs.sort()
    logs_phase = [list(map(int, i.replace('-', ':').split(':'))) for i in logs]
    adv_time = list(map(int, adv_time.replace('-', ':').split(':')))

    # 2.
    # logs의 시작 ~ adv_time 까지의 길이와 겹치는 부분이 있는 지 확인하고
    # 겹치는 부분의 시간을 더해서 가장 큰 값을 가지는 부분의 시작 시간을 반환
    length_history = []
    for i in range(len(logs_phase)):
        between_start = calculate(*logs_phase[i][:3])
        between_end = between_start + calculate(*adv_time)
        logs_phase_end = calculate(*logs_phase[i][3:6])
        length = 0

        if logs_phase_end > between_end:
            length = calculate(*adv_time)
        else:
            length = logs_phase_end - between_start
        for j in range(i + 1, len(logs_phase)):
            next_start = calculate(*logs_phase[j][:3])
            next_end = calculate(*logs_phase[j][3:6])

            # 시작점이 between의 끝 값보다 크면 겹치지 않으므로 break
            if next_start >= between_end:
                break
            else:
                if next_end > between_end:
                    length += (between_end - next_start)
                else:
                    length += (next_end - next_start)
        length_history.append(length)

    return logs[length_history.index(max(length_history))][:8]