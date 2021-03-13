#include <stdio.h>

int main(void)
{
	char pal[30];
	int len = 0, i = 0;

	printf("Type a word: ");
	scanf("%s", &pal);

	printf("Typed word is: ");
	printf("%s", pal);
	printf("\n");

	while (pal[i++] != '\0')
		len++;

	for (i = 0; i < len / 2; i++)
	{
		if (pal[i] != pal[len - 1])
			return printf("It is not palindrome");
		len--;
	}

	return printf("It is palindrome");
}