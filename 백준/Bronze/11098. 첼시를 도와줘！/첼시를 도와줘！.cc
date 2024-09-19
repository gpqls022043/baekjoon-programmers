#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int n, p, i, j, c = 0;
	char name[21];
	char result[10000][21] = { 0 };

	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &p);
		int max_price = 0;
		for (j = 0; j < p; j++)
		{
			scanf("%d %s", &c, &name);
			if (c > max_price)
			{
				max_price = c;
				strcpy(result[i], name);
			}

		}
	}

	for (i = 0; i < n; i++)
	{
		printf("%s\n", result[i]);
	}
}

