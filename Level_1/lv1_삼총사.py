def solution(number):
    nums = sorted(number)
    answer = 0
    for idx, num in enumerate(nums):
        for s_idx, s_num in enumerate(nums[idx + 1:]):
            for d_num in nums[idx + s_idx + 2:]:
                if num + s_num + d_num == 0:
                    print(num, s_num, -(num + s_num))
                    answer += 1
                
    return answer