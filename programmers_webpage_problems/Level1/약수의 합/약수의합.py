def divisor_sum(n):
    cnt = 0
    i = 1

    while i <= n / 2:
        if n % i == 0:
            cnt += i
        i += 1
    return cnt + n

def solution(n):
    return divisor_sum(n)
