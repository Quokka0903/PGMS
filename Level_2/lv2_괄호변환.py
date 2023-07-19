def solution(p):
    if not p : return p

    is_correct, count = True, 0
    for i in range(len(p)):
        
        if p[i] == '(':
            count -= 1
        else:
            count += 1
        
        if count > 0:
            is_correct = False
        
        if count == 0:
            if is_correct:
                return p[:i + 1] + solution(p[i + 1:])
                
            else:
                return '(' + solution(p[i + 1:]) + ')' \
                         + ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))