def solution(expression):
    answer = 0
    orders = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]
    
    def calc (num1, num2, c):
        if c == '+':
            return num1 + num2
        elif c == '-':
            return num1 - num2
        else:
            return num1 * num2
    
    nums = []
    giho = []
    
    temp = ''
    for word in expression:
        if word.isdigit():
            temp += word
        else:
            nums.append(int(temp))
            temp = ''
            giho.append(word)
    nums.append(int(temp))
    
    
    for order in orders:
        now_nums = nums
        now_giho = giho
        for c in order:
            temp_nums = [now_nums[0]]
            temp_giho = []
            for idx in range(len(now_giho)):
                if now_giho[idx] == c:
                    temp_nums.append(calc(temp_nums.pop(), now_nums[idx + 1], c))
                else:
                    temp_nums.append(now_nums[idx + 1])
                    temp_giho.append(now_giho[idx])
            
            now_nums = temp_nums
            now_giho = temp_giho
        
        if answer < abs(now_nums[0]):
            answer = abs(now_nums[0])
    
    
    return answer