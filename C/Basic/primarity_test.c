#include <stdio.h>

// 素数判定(真なら0, 偽なら1を返す)
int primarityTest(int num)
{
	int flag = 0;
	int i = 0;
	// 素数かどうかを判定
	for( i=2;i<num;++i ) {
		if( num%i==0 ) {
			flag = 1;
			break;
		}
	}
	return flag;
}

int main(void)
{
	// 変数の宣言
	int num = 3;
	// 判定結果を表示
	if( primarityTest(num)==0 )
		printf("%dは素数",num);
	else
		printf("%dは素数でない",num);

	return 0;
}
