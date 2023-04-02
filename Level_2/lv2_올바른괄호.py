def solution(s):
    answer = True
    stack = []
    gualho = ["(", ")"]
    
    for unit in s:
        if unit == gualho[0]:
            stack.append(unit)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    else:
        return True