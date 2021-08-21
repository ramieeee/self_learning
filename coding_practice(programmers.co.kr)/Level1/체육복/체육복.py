def solution(n, lost, reserve):
    l = [0] * n

    for i in lost:
        l[i - 1] = -1
    for i in reserve:
        if l[i - 1] == 0:
            l[i - 1] = 1
        else:
            l[i - 1] = 0
    for i in range(len(l)):
        try:
            if i == 0:
                if l[i] == 1:
                    if l[i + 1] == -1:
                        l[i + 1] = 0
                        l[i] = 0
            elif l[i] == 1:
                if l[i - 1] == -1:
                    l[i - 1] = 0
                    l[i] = 0
                elif l[i + 1] == -1:
                    l[i + 1] = 0
                    l[i] = 0
        except:
            pass
    return l.count(0) + l.count(1)
