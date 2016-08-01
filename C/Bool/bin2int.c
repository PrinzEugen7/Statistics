#include <stdio.h>

// 2進数(文字列)を10進数(整数)に変換
int bin2int(char bin[]){
    int len=256, i, x=0;
    char buf[33];

    // 文字列の長さを求める(終端コード￥０の位置を探す)
    for (i=0; i<1024; i++){
        if (bin[i]==0){len=i; break;}
    }
    if (len<32){
        // 32bitでない場合は0で詰め物をする
        for (i=0; i<32-len; i++){
            buf[i]='0';
        }
        for (i=0; i<len; i++){
            buf[32-len+i]=bin[i];
        }
        buf[32]=0;
    }
    else{  // 32bitの時はそのままコピー
        for (i=0; i<len; i++){
            buf[i]=bin[i];
        }
    }
    // 不適切な文字が入っていないかチェック
    for(i=0; i<32; i++){
         if (buf[i]!='1' && buf[i]!='0'){
             // 2進数ではない
             return 0; // 不適切な場合は0を返す
         }
    }
    // 変換するための本体：実は次の1行だけが重要
    for(i=31; i>=0; i--) x += (buf[i]-'0')*(1<<(31-i));
    
    return x;
}

int main(void)
{
	char x[7] = {'1', '1', '0', '1', '1', '0', '\0'};
	printf(" x = %s (%d)\n", x, bin2int( x ) );
	return 0;
}
