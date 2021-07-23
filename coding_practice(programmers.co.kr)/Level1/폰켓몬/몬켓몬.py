def solution(nums):
    numlen = len(nums) / 2
    temp = []

    for i in nums:
        if i not in temp:
            temp.append(i)
    ret = len(temp)
    if numlen >= ret:
        return ret
    return numlen
