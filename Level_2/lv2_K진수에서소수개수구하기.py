def solution(n, k):
    words = ""
    while n:
        words = str(n % k) + words
        n = n // k
        
    words = words.split("0")
    
    def is_prime(number):
        for i in range(2, int(number ** 0.5) + 1):
            if not number % i:
                return False
        return True
    
    count = 0
    for word in words:
        if not len(word) or int(word) < 2:
            continue
        
        if is_prime(int(word)):
            count += 1
            
    return count