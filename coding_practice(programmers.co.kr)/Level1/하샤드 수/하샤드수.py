def solution(x):
    ret = 0
    num = x
    
    while num >= 1:
        ret += num % 10
        num = num // 10
    if x % ret == 0:
        return True
    return False
