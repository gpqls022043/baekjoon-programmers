#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int time = 0;
	char ch[16];

	scanf("%s", &ch);

	for (int i = 0; i < strlen(ch); i++)
	{
		if (ch[i] == 'A' || ch[i] == 'B' || ch[i] == 'C') time += 3;
		else if (ch[i] == 'D' || ch[i] == 'E' || ch[i] == 'F') time += 4;
		else if (ch[i] == 'G' || ch[i] == 'H' || ch[i] == 'I') time += 5;
		else if (ch[i] == 'J' || ch[i] == 'K' || ch[i] == 'L') time += 6;
		else if (ch[i] == 'M' || ch[i] == 'N' || ch[i] == 'O') time += 7;
		else if (ch[i] == 'P' || ch[i] == 'Q' || ch[i] == 'R' || ch[i] == 'S') time += 8;
		else if (ch[i] == 'T' || ch[i] == 'U' || ch[i] == 'V') time += 9;
		else if (ch[i] == 'W' || ch[i] == 'X' || ch[i] == 'Y' || ch[i] == 'Z') time += 10;
		else time += 2;

	}

	printf("%d", time);
}