from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer, visitor, time = [], [], []
    record_dict = defaultdict(int)

    for i in records:
        if i[11:] == 'IN':
            visitor.append(i[6:10])
            time.append(int(i[0:2]) * 60 + int(i[3:5]))
        else:
            record_dict[i[6:10]] += int(i[0:2]) * 60 + int(i[3:5]) - time[visitor.index(i[6:10])]
            time.pop(visitor.index(i[6:10]))
            visitor.pop(visitor.index(i[6:10]))

    for i in range(len(visitor)):
        record_dict[visitor[i]] += (1439 - time[i])

    for i in sorted(record_dict.keys()):
        if record_dict[i] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (ceil((record_dict[i] - fees[0]) / fees[2]) * fees[3]))

    return answer