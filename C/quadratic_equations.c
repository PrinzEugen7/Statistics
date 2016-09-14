
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
     
int main()
{
  double d, x;
  double a = 1;
  double b = 2;
  double c = 1;
     
  if (a != 0) {
    b /= a;  c /= a;     // aで割ってx^2 + bx + c = 0$の形にする
    if (c != 0) {
    	b /= 2;          // x^2 + 2b'x + c = 0
    	d = b * b - c;   // 判別式(D/4)を計算
    	if (d > 0) {
    		if (b > 0) x = -b - sqrt(d);
    		else       x = -b + sqrt(d);
    		printf("x = %g, %g\n", x, c / x);
    	} 
    	else if (d < 0)
    		printf("x = %f +- %f\n", -b, sqrt(-d));
    	else
    		printf("x = %f\n", -b);
    	} 
    else printf("x = %f, 0\n", -b);
  } 
  else if (b != 0) printf("x = %f\n", -c / b);
  else if (c != 0) printf("解なし\n");
  else printf("不定\n");
  return 0;
}
