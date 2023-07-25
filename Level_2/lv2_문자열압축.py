def solution(s):
    length = len(s)
    if length == 1:
        return 1
    
    result = []
    for i in range(1, (length // 2) + 1):
        temp = ''
        cnt = 1
        word = s[:i]

        for j in range(i, length, i):
            if word == s[j : i + j]:
                cnt+=1
            else:
                if cnt != 1:
                    temp += str(cnt) + word
                else:
                    temp += word
                word = s[j : j + i]
                cnt = 1
                
        if cnt != 1:
            temp += str(cnt) + word
        else:
            temp += word
                
        result.append(len(temp))
        
    return min(result)