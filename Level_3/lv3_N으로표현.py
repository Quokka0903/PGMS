def solution(N, number):
    res = []
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N) * i))
        
        for j in range(i - 1):
            for unit_1 in res[j]:
                for unit_2 in res[-j - 1]:
                    temp.add(unit_1 + unit_2)
                    temp.add(unit_1 - unit_2)
                    temp.add(unit_1 * unit_2)
                    if unit_2:
                        temp.add(unit_1 / unit_2)
                        
        if number in temp:
            return i
        
        res.append(temp)
    return -1