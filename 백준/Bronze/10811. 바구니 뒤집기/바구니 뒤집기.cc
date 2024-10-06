#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int n, m, a, b, c;
	char ch[100];

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
	{
		ch[i] = i + 1;
	}

	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);

		for (int i = 0; i < (b - a + 1) / 2; i++)
		{
			c = ch[a - 1 + i];
			ch[a - 1 + i] = ch[b - 1 - i];
			ch[b - 1 - i] = c;

		}
	}


	for (int i = 0; i < n; i++)
	{
		printf("%d ", ch[i]);
	}

}