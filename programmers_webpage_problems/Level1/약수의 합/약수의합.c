#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int divisor_cal(int n)
{
    int i = 0;
    int cnt = 0;
    while (++i <= n / 2)
        if (n % i == 0)
            cnt += i;
    return (cnt + n);
}

int solution(int n)
{
    return divisor_cal(n);
}
