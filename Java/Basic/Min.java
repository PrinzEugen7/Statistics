import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
	public static void main( String[] args ) {
    	float min = 100;
		float[] data = { 1, 2, 3, 4, 5};
		// 最小値を求める
		for(int i = 0; i < data.length; i++)
			min = Math.min(min,data[i]);
		System.out.println(min);
	}
}
