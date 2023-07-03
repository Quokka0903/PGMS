def solution(n, cores):

    if n <= len(cores):
        return n
    
    else:
        n -= len(cores)
        left = 1
        right = n * max(cores)

        while left < right:
            mid = (left + right) // 2
            capacity = 0
            
            for core in cores:
                capacity += mid // core
                
            if capacity >= n:
                right = mid
            else:
                left = mid + 1

        for core in cores:
            n -= (right - 1) // core
                
        for idx, unit in enumerate(cores):
            if right % unit == 0:
                n -= 1
                if n == 0:
                    return idx + 1