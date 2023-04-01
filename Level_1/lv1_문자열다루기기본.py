def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for unit in s:
            if unit.isdigit():
                continue
            else:
                answer = False
                break
    else:
         answer = False   
        
    
    
    return answer