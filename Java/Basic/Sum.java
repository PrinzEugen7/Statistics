import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main( String[] args ) {
		double sum = 0;
		double[] data = { 1, 2, 3, 4, 5};
		for( int i=0; i<data.length; i++ ) {
			sum += data[i];
		}
		System.out.println(sum);
	}
}
