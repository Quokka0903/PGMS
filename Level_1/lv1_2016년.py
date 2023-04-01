def solution(a, b):
    mon = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    day = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']
    ans = sum(mon[0 : a - 1]) + b
    return day[ans % 7]