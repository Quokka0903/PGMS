def solution(n, m):
    
    def yak(x, y):
        for i in range(min(x, y), 0, -1):
            if x % i or y % i:
                continue
            else:
                return i
    yaks = yak(n, m)
    baes = n * m // yaks
    answer = [yaks, baes]
    return answer