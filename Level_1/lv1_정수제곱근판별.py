def solution(n):
    
    if n == 1:
        answer = 4
    elif n == 2:
        answer = -1
    else:
        left = 2
        right = n
        answer = -1
        while left < right:
            middle = (left + right) // 2
            if middle**2 > n:
                right = middle
            elif middle**2 < n:
                left = middle + 1
            else:
                answer = (middle + 1) ** 2
                break
    
    return answer