def solution(scoville, K):
    answer = 0
    import heapq
    
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_1 + min_2 * 2)
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer