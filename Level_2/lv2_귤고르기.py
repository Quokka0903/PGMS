def solution(k, tangerine):
    package = {}
    for unit in tangerine:
        if unit not in package:
            package[unit] = 1
        else:
            package[unit] += 1
    
    _package = []
    for unit in package:
        _package.append([package[unit], unit])
    _package.sort(reverse=True)
    
    answer = 0
    for unit in _package:
        k -= unit[0]
        answer += 1
        if k <= 0:
            break
            
    return answer