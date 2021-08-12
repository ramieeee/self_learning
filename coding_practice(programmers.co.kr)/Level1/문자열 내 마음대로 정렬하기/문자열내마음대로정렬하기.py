def compare(str1, str2, n):
    for i in range(n, len(str1)):
        if str1[i] < str2[i]:
            return 1
    return 0

def solution(strings, n):
    ret = strings

    for i in range(len(ret)):
        for j in range(len(ret)):
            if compare(ret[j], ret[j - 1], n) == 1:
                ret[j], ret[j - 1] = ret[j - 1], ret[j]
    return ret
