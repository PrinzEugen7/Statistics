import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
        public static void main( String[] args ) {
                int sum = 0;
                int[] data = { 1, 2, 3, 4, 5};
                for( int i=0; i<data.length; i++ ) {
                        sum += data[i];
                }
                float ave = ( (float)sum )/data.length;
                System.out.println(ave);
        }
}
