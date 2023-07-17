 def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    count = {}
    index = {}
    for idx, unit in enumerate(id_list):
        index[unit] = idx
        count[idx] = [0, []]
        
    for unit in report:
        user = unit.split(" ")
        sue = index[user[0]]
        sued = index[user[1]]
        
        if sue not in count[sued][1]:
            count[sued][1].append(sue)
            count[sued][0] += 1
    
    for unit in count:
        if count[unit][0] >= k:
            for idx in count[unit][1]:
                answer[idx] += 1
    
    return answer