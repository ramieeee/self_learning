def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += i
        elif ord(i) >= 97 <= 122:
            if n + ord(i) > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        elif ord(i) >= 65 <= 90:
            if n + ord(i) > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
    return answer
