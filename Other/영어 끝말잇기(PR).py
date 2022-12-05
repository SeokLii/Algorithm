def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        now_word = words[i]
        before_word = words[i - 1]

        # 이전 단어의 끝과 지금 단어의 첫이 같은지 확인
        if before_word[len(before_word) - 1] != now_word[0]:
            return [(i + 1) % n if (i + 1) % n != 0 else n, (i // n) + 1]
        # 이전 words에 지금 단어가 포함되어 있는지 확인
        elif now_word in words[:i]:
            return [(i + 1) % n if (i + 1) % n != 0 else n, (i // n) + 1]

    return answer