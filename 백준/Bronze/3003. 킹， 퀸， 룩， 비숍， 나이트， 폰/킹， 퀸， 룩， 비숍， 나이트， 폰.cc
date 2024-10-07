#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int k, q, l, b, n, p;
	char chess[6] = { 0 };

	scanf("%d %d %d %d %d %d", &k, &q, &l, &b, &n, &p);

	if (k == 1) chess[0] = 0;
	else chess[0] = 1 - k;

	if (q == 1) chess[1] = 0;
	else chess[1] = 1 - q;

	if (l == 2) chess[2] = 0;
	else chess[2] = 2 - l;

	if (b == 2) chess[3] = 0;
	else chess[3] = 2 - b;

	if (n == 2) chess[4] = 0;
	else chess[4] = 2 - n;

	if (p == 8) chess[5] = 0;
	else chess[5] = 8 - p;

	for (int i = 0; i < 6; i++)
	{
		printf("%d ", chess[i]);
	}
}