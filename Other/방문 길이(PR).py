# 위치 변환 클래스
def change(here, head):
    if head == 'U' and here[1] < 5:
        here[1] += 1
    elif head == 'D' and here[1] > -5:
        here[1] -= 1
    elif head == 'R' and here[0] < 5:
        here[0] += 1
    elif head == 'L' and here[0] > -5:
        here[0] -= 1


def solution(dirs):
    history = []
    here = [0, 0]

    # 캐릭터가 처음 걸어본 길의 길이 == 총 걸어본 길 - 중복되게 걸어본 길
    # set 활용하여 중복 값 제거
    for i in dirs:
        # 깊은 복사로 이전 위치 저장
        before = list(here)

        # 위치 변경
        change(here, i)

        # 위치가 변경되었을 때만 넣어줌
        # ->, <- 방향에서 동일한 길에 접근할 수 있으므로 모두 넣어줌
        if before != here:
            history.append(''.join(list(map(str, before)) + list(map(str, here))))
            history.append(''.join(list(map(str, here)) + list(map(str, before))))

    return len(set(history)) // 2

