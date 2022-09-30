import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      StringBuilder sb = new StringBuilder();
      
     int[] chess = {1,1,2,2,2,8};
     
     for(int i=0; i<6; i++) {
         int now = Integer.parseInt(st.nextToken());
    	 sb.append((chess[i]-now)+" ");
     }
        System.out.print(sb);  
    }
}




/*import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
     int[] chess = {1,1,2,2,2,8};
     
     for(int i=0; i<6; i++) {
    	 int now = sc.nextInt();
    	 System.out.print((chess[i]-now)+" ");
    	 }
          
    }
}*/
