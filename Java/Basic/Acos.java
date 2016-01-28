import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
    public static void main( String[] args ) {
    	double deg = 30;
    	double rad = Math.toRadians(deg);
		double ans = Math.acos(rad);
        System.out.println(ans);
    }
}
