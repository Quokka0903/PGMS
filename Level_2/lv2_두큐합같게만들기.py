from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum_q1 = sum(queue1)
    total = sum_q1 + sum(queue2)
    if total % 2:
        return -1
    while sum_q1 != total//2:
        if answer > len(queue1) + len(queue2):
            return -1
        while queue2 and sum_q1 < total//2:
            queue1.append(queue2.popleft())
            sum_q1 += queue1[-1]
            answer += 1
        while queue1 and sum_q1 > total//2:
            queue2.append(queue1.popleft())
            sum_q1 -= queue2[-1]
            answer += 1
            
    return answer