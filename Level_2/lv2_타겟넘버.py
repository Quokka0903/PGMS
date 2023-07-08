def solution(numbers, target):
    answers = []
    def check_target(idx, now):
        if idx >= len(numbers):
            if now == target:
                answers.append(now)
            return
        
        check_target(idx + 1, now + numbers[idx])
        check_target(idx + 1, now - numbers[idx])
    
    check_target(0, 0)
    
    return len(answers)