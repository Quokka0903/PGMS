def solution(progresses, speeds):
    answer = []
    days = []
    len_p = len(progresses)
    for idx in range(len_p):
        if (100 - progresses[idx]) % speeds[idx]:
            days.append((100 - progresses[idx]) // speeds[idx] + 1)
        else:
            days.append((100 - progresses[idx]) // speeds[idx])
    
    i = 0
    cnt = 0
    while i < len_p:
        idx = i
        while (idx < len_p) and (days[i] >= days[idx]) :
            cnt += 1
            idx += 1
        answer.append(cnt)
        cnt = 0
        i = idx
        
    return answer


# 모범답안

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]