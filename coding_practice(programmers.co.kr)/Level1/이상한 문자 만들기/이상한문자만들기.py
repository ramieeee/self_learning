def solution(s):
    answer = ''
    j = 0
    for i in s:
        if i == ' ':
            j = 1
        if j % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        j += 1
    return answer
