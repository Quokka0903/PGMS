def solution(arr):
    answer = [arr[0]]
    for unit in arr[1:]:
        if unit != answer[-1]:
            answer.append(unit)
    
    return answer