def solution(record):
    answer = []
    sub_record = []
    nicname = {}

    # 이름 변경: enter or change 할 때마다 update
    # 입장 퇴장: sub_record에 아이디와 입장 퇴장 데이터 같이 저장
    for i in record:
        data = i.split()
        if data[0] == 'Enter':
            nicname.update({data[1]: data[2]})
            sub_record.append([data[1], '님이 들어왔습니다.'])
        elif data[0] == 'Leave':
            sub_record.append([data[1], '님이 나갔습니다.'])
        elif data[0] == 'Change':
            nicname.update({data[1]: data[2]})

    # 최종적으로 저장된 nicname을 보고 닉네임을 변경해줌
    for i in sub_record:
        answer.append(nicname[i[0]] + i[1])

    return answer