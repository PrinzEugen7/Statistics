import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
    public static void main( String[] args ) {
    float sum = 0;
    float var = 0;
    float[] data = { 1, 2, 3, 4, 5};
    for(int i=0; i<data.length; i++ ) {
        sum += data[i];
    }
    float ave = ( (float)sum )/data.length;
    for (int i=0; i<data.length; i++) {
        var += ((data[i] - ave)*(data[i] - ave));
    }
    System.out.println(var);
    }
}
