def solution(d, budget):
    answer = 0
    for unit in sorted(d):
        if unit > budget:
            break
        budget -= unit
        answer += 1
    
    return answer