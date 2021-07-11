def solution(a, b):
    answer = 0
    if b > a:
        i = b - a + 1
        while i != 0:
            answer += a
            a += 1
            i -= 1
    else:
        i = a - b + 1
        while i != 0:
            answer += b
            b += 1
            i -= 1
    return answer
