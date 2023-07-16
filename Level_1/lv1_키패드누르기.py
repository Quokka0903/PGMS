def solution(numbers, hand):
    keypad = { 1 : [0,0], 2 : [0,1], 3 : [0,2],
            4 : [1,0], 5 : [1,1], 6 : [1,2],
            7 : [2,0], 8 : [2,1], 9 : [2,2],
           '*' : [3,0], 0 : [3,1], '#' : [3,2] }
    answer = ''
    
    left = keypad['*']
    right = keypad['#']
    
    for number in numbers:
        now = keypad[number]
        
        if number in [1, 4, 7]:
            left = now
            answer += 'L'
            
        elif number in [3, 6, 9]:
            right = now
            answer += 'R'
            
        else:
            left_dist = 0
            right_dist = 0
            
            for x, y, z in zip(left, right, now):
                left_dist += abs(x - z)
                right_dist += abs(y - z)
            
            if left_dist > right_dist:
                right = now
                answer += 'R'
            
            elif left_dist < right_dist:
                left = now
                answer += 'L'
                
            else:
                if hand == 'right':
                    right = now
                    answer += 'R'
                    
                else:
                    left = now
                    answer += 'L'
                    
    return answer