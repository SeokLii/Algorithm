def solution(name, yearning, photo):
    answer = []
    sum_year = sum(yearning)
    hashNY = dict(zip(name, yearning))
    Sname = set(name)
    Sphoto = [set(i) for i in photo]
    for notin in Sphoto:
        sum_notin = 0
        for i in Sname - notin:
            sum_notin += hashNY[i]
        answer.append(sum_year - sum_notin)
    
    return answer
