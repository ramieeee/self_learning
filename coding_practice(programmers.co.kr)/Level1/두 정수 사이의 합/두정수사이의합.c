#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b)
{
    long long answer = 0;
    if (a > b)
    {
        int i = a - b;
        for (; i + 1 != 0; i--)
        {
            answer += b;
            b++;
        }
        return (answer);
    }
    for (int i = b - a; i + 1 != 0; i--)
        {
            answer += a;
            a++;
        }   
    return answer;
}
