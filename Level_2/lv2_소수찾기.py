def solution(numbers):
    
    def is_prime_number(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def make_number(idx, now, cnt):
        if cnt == 0:
            if now != "":
                _now = int(now)
                if (_now not in lists) and is_prime_number(_now):
                    lists.append(_now)
                    return
            return
        
        for i in range(len(numbers)):
            if i in idx:
                continue
            make_number(idx + [i], now + numbers[i], cnt - 1)
            make_number(idx + [i], now, cnt - 1)
            
    lists = []
    make_number([], "", len(numbers))
    #print(lists)
    
    return len(lists)