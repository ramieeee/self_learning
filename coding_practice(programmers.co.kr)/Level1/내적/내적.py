def solution(a, b):
    i = 0
    answer = 0
    while (i < len(a)):
        answer += (a[i] * b[i])
        i += 1
    return answer
