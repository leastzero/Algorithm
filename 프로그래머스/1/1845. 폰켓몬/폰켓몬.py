def solution(nums):
    set_nums = set(nums)
    if len(set_nums) > len(nums) / 2:
        answer = len(nums) / 2
    else:
        answer = len(set_nums)
    return answer