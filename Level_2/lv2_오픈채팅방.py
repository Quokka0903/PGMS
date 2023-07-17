def solution(record):
    answer = []
    users = {}
    ments = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    stack = []
    for word in record:
        position = word.split(" ")
        if position[0] == "Change":
            users[position[1]] = position[2]
        else:
            if position[0] == "Enter":
                users[position[1]] = position[2]
            stack.append([position[1], position[0]])
    
    for entity in stack:
        answer.append(users[entity[0]] + ments[entity[1]])
    
    return answer