def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            answer += s[i]
        elif s[i] == 'o' and s[i - 1] == 'r' and s[i - 2] == 'e':
            answer += '0'
        elif s[i] == 'e' and s[i - 1] == 'n' and s[i - 2] == 'o':
            answer += '1'
        elif s[i] == 'o' and s[i - 1] == 'w' and s[i - 2] == 't':
            answer += '2'
        elif s[i] == 'e' and s[i - 1] == 'e' and s[i - 2] == 'r' and s[i - 3] == 'h':
            answer += '3'
        elif s[i] == 'r' and s[i - 1] == 'u' and s[i - 2] == 'o' and s[i - 3] == 'f':
            answer += '4'
        elif s[i] == 'e' and s[i - 1] == 'v' and s[i - 2] == 'i' and s[i - 3] == 'f':
            answer += '5'
        elif s[i] == 'x' and s[i - 1] == 'i' and s[i - 2] == 's':
            answer += '6'
        elif s[i] == 'n' and s[i - 1] == 'e' and s[i - 2] == 'v' and s[i - 3] == 'e':
            answer += '7'
        elif s[i] == 't' and s[i - 1] == 'h' and s[i - 2] == 'g' and s[i - 3] == 'i':
            answer += '8'
        elif s[i] == 'e' and s[i - 1] == 'n' and s[i - 2] == 'i' and s[i - 3] == 'n':
            answer += '9'
    return int(answer)
