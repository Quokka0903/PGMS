def solution(k, dungeons):
    dungeons.sort(reverse=True)
    
    answer = []
    def firodo(dun, cnt, left):
        answer.append(cnt)
        if not dun:
            return
        for i in range(len(dun)):
            if dun[i][0] <= left:
                firodo(dun[:i] + dun[i + 1:], cnt + 1, left - dun[i][1])
        
    firodo(dungeons, 0, k)
    
    return max(answer)