def solution(orders, course):
    answer = []
    
    def make_johab(idx, res, cnt, order):
        if not cnt:
            johab.add(res)
            return
        
        if idx < len(order) and cnt >= 1 :
            make_johab(idx + 1, res, cnt, order)
            make_johab(idx + 1, res + order[idx], cnt - 1, order)
    
    for foods in course:
        johab = set([])
        for order in orders:
            make_johab(0, "", foods, sorted(order))
        #print("johab", johab)
        count = {}
        for unit in johab:
            for order in orders:
                if len(set((unit + order))) == len(order):
                    if unit in count:
                        count[unit] += 1
                    else:
                        count[unit] = 1
                        
        #print("count", count)
        if count:
            result = sorted(count, key = lambda x : (-count[x]))
            max_cnt = count[result[0]]
            if max_cnt > 1:
                for check in count:
                    if count[check] == max_cnt:
                        answer.append(check)
    
    return sorted(answer)