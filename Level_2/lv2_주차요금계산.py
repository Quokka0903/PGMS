def solution(fees, records):
    answer = []
    cars = {}
    
    def time_cal(time):
        _time = time.split(":")
        return int(_time[0]) * 60 + int(_time[1])
    
    for record in records:
        data = record.split(" ")
        if data[1] not in cars:
            cars[data[1]] = [time_cal(data[0]), 0, 1]
        else:
            if cars[data[1]][2]:
                cars[data[1]] = [0, cars[data[1]][1] + time_cal(data[0]) - cars[data[1]][0], 0]
            else:
                cars[data[1]] = [time_cal(data[0]), cars[data[1]][1], 1]
            
    for car in sorted(cars):
        if cars[car][2]:
            cars[car][1] = cars[car][1] + (1439 - cars[car][0])
        
        if cars[car][1] <= fees[0]:
            answer.append(fees[1])
            
        else:
            total = cars[car][1] - fees[0]
            
            if total % fees[2]:
                answer.append(fees[1] + (total // fees[2] + 1) * fees[3])
            else:
                answer.append(fees[1] + (total // fees[2]) * fees[3])

    return answer