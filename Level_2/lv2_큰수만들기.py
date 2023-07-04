def solution(number, k):
    
    answer = ""
    
    for unit in number:
        if answer and answer[-1] < unit:
            while answer and answer[-1] < unit and k > 0:
                k -= 1
                answer = answer[:-1]
        answer += unit
    
    if k > 0:
        answer = answer[:-k]
    
    return answer