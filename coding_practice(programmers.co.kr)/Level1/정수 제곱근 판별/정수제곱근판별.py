def solution(n):
    for i in range(n // 2 + 1):
        if n / i == float(i):
            return int((i + 1) * (i + 1))
    return -1
