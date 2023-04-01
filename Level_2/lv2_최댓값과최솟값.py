def solution(s):
    nums = sorted(list(map(int, s.split(" "))))
    def int_to_str(n):
        if n >= 0:
            return str(n)
        else:
            return "-" + str(-n)
                  
    answer = int_to_str(nums[0]) + " " + int_to_str(nums[-1])
    return answer