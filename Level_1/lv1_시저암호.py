def solution(s, n):
    
    def pw(word):
        idx = ord(word) + n
        if word.isupper():
            return chr(idx) if chr(idx).isupper() else chr(idx - 26)
        else:
            return chr(idx) if chr(idx).islower() else chr(idx - 26)
    
    answer = ''
    for unit in s:
        if unit.isalpha():
            answer += pw(unit)
        else:
            answer += unit
            
    return answer