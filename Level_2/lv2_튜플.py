def solution(s):
    check = ['{', '}', ',']
    cnt = {}
    
    temp = ''
    for word in s:
        if word not in check:
            temp += word
        else:
            if temp:
                if int(temp) not in cnt:
                    cnt[int(temp)] = 1
                else:
                    cnt[int(temp)] += 1
            temp = ''

    return sorted(cnt, key = lambda x : cnt[x], reverse=True)