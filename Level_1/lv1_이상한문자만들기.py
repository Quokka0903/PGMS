def solution(s):
    answer = ''
    cnt = 0
    for unit in s:
        if unit == " ":
            answer += unit
            cnt = 0
        else:
            if cnt % 2 == 0:
                if unit.islower():
                    answer += chr(ord(unit) - 32)
                else:
                    answer += unit
            else:
                if unit.isupper():
                    answer += chr(ord(unit) + 32)
                else:
                    answer += unit
            cnt += 1
            
    return answer