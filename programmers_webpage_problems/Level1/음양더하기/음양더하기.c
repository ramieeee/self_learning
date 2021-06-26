#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int *absolutes, int absolutes_len, bool *signs, int signs_len)
{    
    int answer = 0;
    int i = -1;
    
    while (++i < absolutes_len)
    {
        if (signs[i] == false)
            absolutes[i] *= -1;
        answer += absolutes[i];
    }
    return answer;
}
