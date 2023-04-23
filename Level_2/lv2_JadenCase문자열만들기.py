def solution(s):
    answer = ''
    _ans = list(s.split(" "))
    for unit in _ans:
        if unit != "":
            answer += unit[0].upper() + unit[1:].lower() + " "
        else:
            answer += " "
            
    return answer[:-1]