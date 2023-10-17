def solution(triangle):
    hap = [triangle[0]]
    for floor in range(1, len(triangle)):
        hap.append([])
        
        for i in range(len(triangle[floor])):
            if i == 0:
                hap[floor].append(hap[floor-1][0] + triangle[floor][0])
                
            elif i == len(triangle[floor]) - 1:
                hap[floor].append(hap[floor-1][i-1] + triangle[floor][i])
                
            else:
                hap[floor].append(max(hap[floor-1][i-1], hap[floor-1][i]) + triangle[floor][i])
    
    return max(hap[floor])