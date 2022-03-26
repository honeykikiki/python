#include <stdio.h>
#include <string.h>
#include <windows.h>
#include  <stdlib.h>
#include <windows.h>
#include <time.h>

#define MAX 10
#define NUM 10

int main()
{
	int a, i, k;
	int hap = 0;
	
	int List[NUM];

	char name[MAX][10] = {"이성민", "조현준", "오세진", "허성진", "조형민", "힐탑", "청년부"};

    srand((unsigned)time(NULL));


	printf("숫자 1 - 7 중에서 하나를 선택하신후, 입력해주세요.\n:");
	scanf_s("%d", &a);

	switch (a)
	{
	case 1:
		for (i = 1; i <= 1; i++)
		{
			for (k = 1; k <= 9; k++)
			{
				printf("%d X %d = %d\n", i, k, i * k);
			}
		}
		break;

	case 2:
		for (i = 1; i <= 10; i++)
		{
			if (i % 2 != 0)
				continue;

			hap += i;
		}
		printf(": %d\n", hap);
		break;

	case 3:
		for (int i = 0; i < 1; i++) {

			int idx = 0;

			int number = rand() % MAX;

			List[i] = number;

		}
		for (int i = 0; i < 1; i++) {

			printf("%d\t%s\n", i, name[List[i]]);

		}
		break;
	case 4:
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (j == i)
					printf("****");
				else
					printf(" ");
			}
			printf("\n");
		}
		return 0;
		break;
	case 5:
		
			printf("숫자 1 - 7 중에서 하나를 선택하신후, 입력해주세요.\n:");
			scanf_s("%d", &a);
		if(a = 1)
			for (i = 1; i <= 1; i++)
			{
				for (k = 1; k <= 9; k++)
				{
					printf("%d X %d = %d\n", i, k, i * k);
				}
			}
		if(a = 2)
			for (i = 1; i <= 10; i++)
			{
				if (i % 2 != 0)
					continue;

				hap += i;
			}
		printf(": %d\n", hap);
		if(a = 3)
			for (int i = 0; i < 1; i++) {

				int idx = 0;

				int number = rand() % MAX;

				List[i] = number;

			}
		for (int i = 0; i < 1; i++) {

			printf("%d\t%s\n", i, name[List[i]]);

		}
		if(a = 4)
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (j == i)
						printf("****");
					else
						printf(" ");
				}
				printf("\n");
			}

		if(a = 6)
			Sleep(1000);
		printf("hellow\n");
		Sleep(3000);
		printf("world!");
		if(a = 7)
		break;

	case 6:
		Sleep(1000);
		printf("hellow\n");
		Sleep(3000);
		printf("world!");
		break;

	case 7:
		/*system("shutdown -s -t 0");*/
		//콘솔 종료를 못찾고 컴퓨터 종료를 찾았아요.
		break;

	}
}