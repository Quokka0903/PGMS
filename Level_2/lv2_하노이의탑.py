def solution(n):
    answer = []
    
    def hanoi(source, target, via, n):
        if n == 1:
            answer.append([source, target])
        else:
            hanoi(source, via, target, n-1)
            hanoi(source, target, via, 1)
            hanoi(via, target, source, n-1)
            
    hanoi(1, 3, 2, n)
    
    return answer