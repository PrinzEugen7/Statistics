#include <stdio.h>

// 桁数を計算
int calcDigit(int num)
{
	int digit = 0;
	while(num!=0){
		num = num / 10;
		digit++;
	}
	return digit;
}

int main(void)
{
    int num = 777;
    printf("%dの桁数は%d\n", num, calcDigit(num));
    return 0;
}
