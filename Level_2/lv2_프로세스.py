def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        res = queue.pop(0)
        if any(res[1] < q[1] for q in queue):
            queue.append(res)
        else:
            answer += 1
            if res[0] == location:
                return answer