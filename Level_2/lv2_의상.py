def solution(clothes):
    answer = 1
    dic = {}
    for unit in clothes:
        if unit[1] in dic:
            dic[unit[1]] += 1
        else:
            dic[unit[1]] = 1
    
    for unit in dic:
        answer *= (dic[unit] + 1)
    
    return answer - 1