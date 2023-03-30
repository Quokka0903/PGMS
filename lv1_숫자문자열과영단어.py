def solution(s):
    l = ""
    su = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            l += s[idx]
            idx += 1
        else:
            check = ""
            while check not in su:
                check += s[idx]                
                idx += 1
            for sIdx, unit in enumerate(su):
                if check == unit:
                    l += str(sIdx)
                    check = ""
                    break
            
    answer = int(l)
    return answer