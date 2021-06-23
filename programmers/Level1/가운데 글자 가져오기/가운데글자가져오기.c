#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int len(char *str)
{
    int i = 0;
    while (*str)
    {
        str++;
        i++;
    }
    return (i);
}

char *solution(const char *str)
{
    char *answer = (char*)malloc(sizeof(char) * 3);
    int i = len(str) / 2;
    if (len(str) % 2 == 0)
    {
        answer[0] = str[i - 1];
        answer[1] = str[i];
        answer[2] = 0;
        return (answer);
    }
    answer[0] = str[i];
    answer[1] = 0;
    return (answer);
}
