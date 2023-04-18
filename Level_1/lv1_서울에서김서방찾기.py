def solution(seoul):
    res = ''
    for idx, unit in enumerate(seoul) :
        if unit == 'Kim':
            res += str(idx)
    answer = '김서방은 ' + res + '에 있다'
    return answer