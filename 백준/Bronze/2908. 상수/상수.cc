#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char n1[4], n2[4];
	int c = 0;
	int num1 = 0;
	int num2 = 0;
	int i = 0;

	scanf("%s %s", &n1, &n2);

	num1 = (n1[2] - 48) * 100 + (n1[1] - 48) * 10 + (n1[0] - 48);
	num2 = (n2[2] - 48) * 100 + (n2[1] - 48) * 10 + (n2[0] - 48);

	if (num1 > num2) printf("%d", num1);
	else if (num1 < num2) printf("%d", num2);

	return 0;
}