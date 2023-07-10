def solution(N, stages):
    answer = []
    rate = [[i + 1, 0] for i in range(N)]
    
    players = len(stages)
    for idx in range(1, N + 1):
        if players:
            now = stages.count(idx)
            rate[idx - 1][1] = now / players
            players -= now
    
    for stage in sorted(rate, key = lambda x : -x[1]):
        answer.append(stage[0])
    
    return answer