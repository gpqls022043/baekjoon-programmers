#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n;
	int space_n, star_n;

	scanf("%d", &n);

	for (int i = 0; i < (2 * n - 1); i++)
	{
		space_n = n - 1 - i;
		star_n = 1 + (i * 2);

		if (space_n < 0)
		{
			space_n = i - n + 1;
			star_n = (n - 1) * 2 - 1 + (i - n)* (-2);

			for (int i = 0; i < space_n; i++)
			{
				printf(" ");
			}
			for (int j = 0; j < star_n; j++)
			{
				printf("*");
			}
			printf("\n");
		}

		else
		{
			for (int i = 0; i < space_n; i++)
			{
				printf(" ");
			}
			for (int j = 0; j < star_n; j++)
			{
				printf("*");
			}
			printf("\n");
		}
	}
}