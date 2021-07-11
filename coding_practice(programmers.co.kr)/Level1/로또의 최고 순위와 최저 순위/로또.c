#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int *solution(int *lottos, int lottos_len, int *win_nums, int win_nums_len)
{
    int* answer = (int*)malloc(2 * sizeof(int));
    int zero_count = 0;
    int i = -1;
    int win_count = 0;
    
    while (++i < lottos_len)
    {
        if (lottos[i] == 0)
            zero_count++;
        int j = -1;
        while (++j < win_nums_len)
            if (lottos[i] == win_nums[j])
                win_count++;
    }
    if (zero_count + win_count == 0)
        answer[0] = 6;
    else
        answer[0] = 7 - (zero_count + win_count);
    if (win_count == 0)
        answer[1] = 6;
    else
        answer[1] = 7 - win_count;
    return answer;
}
