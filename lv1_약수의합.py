def solution(n):
    yaksu = 1
    answer = 0
    while n >= yaksu:
        if not (n%yaksu):
            answer += yaksu
        yaksu += 1
        
    return answer