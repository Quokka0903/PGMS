def solution(bridge_length, weight, truck_weights):
    stack = [0 for _ in range(bridge_length)]
    now_time = 0
    now_weight = 0
    
    while stack:
        
        now_time += 1
        now_weight -= stack.pop(0)
        
        if truck_weights:
            if now_weight + truck_weights[0] <= weight:            
                truck = truck_weights.pop(0)
                stack.append(truck)
                now_weight += truck
            else:
                stack.append(0)
                 
    return now_time