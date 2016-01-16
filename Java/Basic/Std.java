import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
    public static void main( String[] args ) {
        double sum = 0;
        double var = 0;
        double[] data = { 1, 2, 3, 4, 5};
        double n = data.length;
        for(int i=0; i<data.length; i++ ) {
            sum += data[i];
        }
        double ave = ( (double)sum )/data.length;
        for (int i=0; i<data.length; i++) {
            var += ((data[i] - ave)*(data[i] - ave));
        }
       double std = Math.sqrt(var/n);
       System.out.println(std);
    }
}
