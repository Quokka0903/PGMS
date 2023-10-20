def solution(n, computers):
    net_count = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        net_count += 1
        stack = [i]
        while stack:
            here = stack.pop()
            for index in range(len(computers[here])):
                if computers[here][index] == 1 and visited[index] == 0:
                    visited[index] = net_count
                    stack.append(index)
                    
    return net_count