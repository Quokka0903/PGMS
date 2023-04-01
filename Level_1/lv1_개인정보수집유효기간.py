def solution(today, terms, privacies):
    Y, M, D = map(int, (today.split('.')))
    term_dict = {}
    for term in terms:
        types, times = term.split(' ')
        term_dict[types] = int(times)
    
    answer = []
    for idx, privacy in enumerate(privacies):
        pY, pM, pD = map(int, (privacy[0:-2].split('.')))
        pM += term_dict[privacy[-1]]
        if pM > 12:
            if pM%12:
                pY += (pM // 12)
                pM %= 12
            else:
                pY += (pM // 12 - 1)
                pM = 12
        
        if (Y > pY) or (Y == pY and M > pM) or (Y == pY and M == pM and D >= pD):
            answer.append(idx+1)
    
    return answer