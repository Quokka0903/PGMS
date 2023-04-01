def solution(lottos, win_nums):
    sunwi = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero = 0
    for unit in lottos:
        if unit in win_nums:
            cnt += 1
        if unit == 0:
            zero += 1
    
    
    answer = [sunwi[cnt + zero], sunwi[cnt]]
    return answer