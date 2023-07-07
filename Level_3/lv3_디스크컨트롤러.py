from heapq import heappop, heappush

def solution(jobs):

    past = -1
    now = 0
    
    idx = 0
    total = 0
    heap = []
    
    while idx < len(jobs):
        for job in jobs:
            if past < job[0] <= now:
                heappush(heap, [job[1], job[0]])
        
        #print(heap)
        
        if heap:
            best = heappop(heap)
            past, now = now, now + best[0]
            total += now - best[1]
            idx += 1
        else:
            now += 1
            
        #print(idx, now, total)
    
    return total // len(jobs)