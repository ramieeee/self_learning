import math
def solution(answers):
    answer = []
    f = 0
    s = 0
    t = 0
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l1 = math.ceil(len(answers) / len(first))
    l2 = math.ceil(len(answers) / len(second))
    l3 = math.ceil(len(answers) / len(third))
    
    first *= l1
    second *= l2
    third *= l3
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            f += 1
        if answers[i] == second[i]:
            s += 1
        if answers[i] == third[i]:
            t += 1
    answer = [f, s, t]
    ret = []
    if answer.count(max(answer)) == 1:
        answer = [answer.index(max(answer)) + 1]
        return answer
    else:
        for j in range(len(answer)):
            if answer[j] == max(answer):
                ret.append(j + 1)
    return ret
