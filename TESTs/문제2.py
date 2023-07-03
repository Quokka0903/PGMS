def solution(a, b, g, s, w, t):
    left = 0
    right = 2 * 2 * 10**5 * 10**9
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        gold = 0
        silver = 0
        total = 0
        
        for idx in range(len(g)):
            moves   = (mid // (t[idx] * 2)) + 1  if mid % (t[idx] * 2) >= t[idx]         else (mid // (t[idx] * 2))
            gold    += w[idx] * moves            if w[idx] * moves <= g[idx]             else g[idx]
            silver  += w[idx] * moves            if w[idx] * moves <= s[idx]             else s[idx]
            total   += w[idx] * moves            if w[idx] * moves <= g[idx] + s[idx]    else g[idx] + s[idx]
            
        if a > gold or b > silver or a + b > total:
            left = mid + 1
            
        else:
            right = mid - 1
            answer = min(mid, answer)
    
    return answer