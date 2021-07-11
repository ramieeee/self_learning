#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char *str_cat(char *dest, char *src)
{
    while(*dest)
        dest++;
    while (*src)
        *(dest++) = *(src++);
    *dest = 0;
    return (dest);
}

char *solution(int n)
{
    char *answer = (char*)malloc(n * 3 + 1);
    int i = -1;
    char *s = "수";
    char *b = "박";
    
    while (++i < n)
        answer[i] = 0;
    i = -1;
    while (++i < n)
    {
        if (i % 2 == 0)
            str_cat(answer, s);
        else
            str_cat(answer, b);
    }
    return (answer);
}
