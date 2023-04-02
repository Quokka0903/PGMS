# def solution(number, limit, power):
    
#     yaks = [0] * (number + 1)
    
                  
#     def yak(num, limit):
#         cnt = 0
#         for i in range(num, 0, -1):
#             if num % i == 0:
#                 cnt += 1
#             if cnt > limit:
#                 return power
#             i -= 1
#         return cnt
    
#     answer = 0    
#     for num in range(1, number + 1):
#         answer += yak(num, limit)
    
#     return answer

# 또 시초떠서 리팩토링

def solution(number, limit, power):
    
    def yak(num, limit):
        cnt = 0
        for i in range(1, num + 1):
            if i**2 > num:
                break
            if num % i == 0:
                cnt += 1
                if num != i**2:
                    cnt += 1
            if cnt > limit:
                return power
            
        return cnt
    
    answer = 0    
    for num in range(1, number + 1):
        answer += yak(num, limit)
    
    return answer