def solution(plans):
    def timeCha(a, b):
        si = int(a[:2]) - int(b[:2])
        bun = int(a[3:]) - int(b[3:])
        return si * 60 + bun
    
    answer = []
    plans.sort(key = lambda x : x[1], reverse=True)
    
    stack = []
    stack.append(plans.pop())
    stack[-1][-1] = int(stack[-1][-1])
    time = stack[0][1]
    while plans:
        stack.append(plans.pop())
        stack[-1][-1] = int(stack[-1][-1])
        cha, time = timeCha(stack[-1][1], time), stack[-1][1]
        
        for idx in range(len(stack)-2 , -1 , -1):
            stack[idx][2] = stack[idx][2] - cha
            if stack[idx][2] <= 0:
                cha = -stack[idx][2]
                answer.append(stack[idx][0])
                stack.remove(stack[idx])
                print(stack)
            else:
                break
        
    while stack:
        answer.append(stack.pop()[0])
                   
    
    return answer