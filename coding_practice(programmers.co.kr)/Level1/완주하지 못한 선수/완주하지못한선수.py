def solution(participant, completion):
    i = sorted(participant)
    j = sorted(completion)
    
    for n in range(len(j)):
        if i[n] != j[n]:
            return i[n]
    return i[n + 1]
