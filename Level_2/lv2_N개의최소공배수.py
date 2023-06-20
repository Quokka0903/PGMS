def solution(arr):
    
    def gcd(n1, n2):
        if not n2 :
            return n1
        else :
            return gcd(n2, n1%n2)
    
    answer = arr[0]
    for unit in arr[1:]:
        answer = answer * unit // gcd(answer, unit)
    return answer