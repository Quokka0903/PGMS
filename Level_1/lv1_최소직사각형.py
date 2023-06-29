def solution(sizes):
    garo = max([max(a, b) for a, b in sizes])
    sero = max([min(a, b) for a, b in sizes])
    return garo * sero