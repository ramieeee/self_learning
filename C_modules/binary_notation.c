#include <stdio.h>

int cal(int num)
{
	if (num == 1)
	{
		printf("%d", 1);
		return;
	}

	else if (num == 2)
	{
		printf("%d%d", 1, 0);
		return;
	}

	else if (num == 3)
	{
		printf("%d%d", 1, 1);
		return;
	}

	else
	{
		cal(num / 2);
		printf("%d", num % 2);
	}
}

int main(void)
{
	int num;

	printf("decimal system input: ");
	scanf("%d", &num);
	printf("\n");

	printf("binary notation print: ");

	cal(num);
}