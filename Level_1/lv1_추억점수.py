def solution(name, yearning, photo):
    answer = []
    for unit in photo:
        if name == unit:
            answer.append(sum(yearning))
        else:
            cnt = 0
            for idx in range (len(name)):
                if name[idx] in unit:
                    cnt += yearning[idx]
            answer.append(cnt)
                
    return answer