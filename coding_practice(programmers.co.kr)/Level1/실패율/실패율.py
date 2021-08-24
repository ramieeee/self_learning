def solution(N, stages):
    stage = [i for i in range(1, N + 1)]

    for i in range(len(stage)):
        for j in range(len(stage) - i - 1):
            sum_p_stage_a = sum([stage.count(n) for n in range(1, stage[j])])
            if sum_p_stage_a == 1 and stage[j] == 1:
                sum_p_stage_a += 1

            sum_p_stage_b = sum([stage.count(n) for n in range(1, stage[j])])
            if sum_p_stage_b == 1 and stage[j + 1] == 1:
                sum_p_stage_b += 1
            
            a = stages.count(stage[j]) / (len(stages) - sum_p_stage_a)
            b = stages.count(stage[j + 1]) / (len(stages) - sum_p_stage_b)
        
            if a > b:
                stage[j], stage[j + 1] = stage[j + 1], stage[j]
            elif a == b:
                if stage[j] > stage[j + 1]:
                    stage[j], stage[j + 1] = stage[j + 1], stage[j]
    return stage
