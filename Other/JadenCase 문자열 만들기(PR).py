def solution(s):
    # 이 문제의 관건은 빈 공백문자에 있고 split()과 split(' ')의 차이를 알아야함
    # split(' ') 공백을 살려서 받아와서 이걸 써야함
    # 따로 리스트를 만들어 주는게 너무 오래 걸릴 수 있음
    # answer = ' '.join([i.capitalize() for i in s.split(' ')])
    sub = s.split(' ')
    cap = []
    for i in sub:
        cap.append(i.capitalize())
    answer = ' '.join(cap)

    print(answer)
    return answer