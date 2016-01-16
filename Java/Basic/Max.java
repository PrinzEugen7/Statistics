import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
	public static void main( String[] args ) {
    		double max = 0;
		double[] data = { 1, 2, 3, 4, 5};
		// 最大値を求める
		for(int i = 0; i < data.length; i++)
			max = Math.max(max,data[i]);
		System.out.println(max);
	}
}
