def solution(brown, yellow):
    a = (brown // 2) - 3
    b = 1
    
    while a >= b:
        print(a, b, yellow)
        if a * b == yellow:
            return [a + 2, b + 2]
        a -= 1
        b += 1
        