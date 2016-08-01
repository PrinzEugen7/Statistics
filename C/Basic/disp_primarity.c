#include <stdio.h>

// 素数判定(真なら0, 偽なら1を返す)
int dispPrimarity(int n1, int n2)
{

	int i = 0;
	int j = 0;
	// 素数判定
	for( i=n1;i<=n2;++i ) {
		int flag = 0;
		for( j=2;j<i;++j ){
			if( i%j==0 ) {
				flag = 1;
				break;
			}
		}
		// 素数なら出力
		if( flag==0 )
			printf("%d ", i);
	}
	return 0;
}

int main(void)
{
	// 5～10までの素数を表示
	dispPrimarity(5, 15);

	return 0;
}
