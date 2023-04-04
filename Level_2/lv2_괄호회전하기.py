def solution(s):
    gualho = {"]" : "[", "}" : "{", ")" : "("}
    def cnt(strs):
        stack = []
        while strs:
            if len(stack) == 0 or strs[0] not in gualho or gualho[strs[0]] != stack[-1]:
                stack.append(strs[0])
                strs = strs[1:]
            else:
                stack = stack[:-1]
                strs = strs[1:]
        return len(stack) == 0
    
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if cnt(s):
            answer += 1
    
    return answer