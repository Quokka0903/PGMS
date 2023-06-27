def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : (str(x) * 3)[:4])
    for unit in numbers[::-1]:
        answer += str(unit)
    
    return answer if answer[0] != "0" else "0"