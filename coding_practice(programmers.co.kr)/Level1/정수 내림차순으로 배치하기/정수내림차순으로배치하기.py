def solution(n):
    answer = str(n)
    answer = sorted(answer, reverse=True)
    return int(''.join(answer))
