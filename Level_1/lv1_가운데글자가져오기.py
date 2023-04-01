def solution(s):
    l = len(s)
    n = l//2
    if l%2:
        return s[n]
    else:
        return s[n-1 : n+1]