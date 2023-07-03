def solution(name):
    answer = 0
    move = len(name)
    
    for idx, word in enumerate(name):
        
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        move = min(move, (2 * idx) + (len(name) - next), 2 * (len(name) - next) + idx)
        
        answer += min(ord(word) - ord("A"), ord("Z") - ord(word) + 1)
            
    return answer + move