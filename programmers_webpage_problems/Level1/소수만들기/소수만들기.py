def is_prime(num):
    if num == 1 or num == 2:
        return 1
    for i in range(num // 2):
        if num % (i + 2) == 0:
            return 0
    return 1

def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]) == 1:
                    answer += 1
    return answer
