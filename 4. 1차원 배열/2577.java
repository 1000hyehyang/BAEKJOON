import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int value = Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine());
        int aa[] = new int[10];
        
        while(value!=0) {
        	aa[value%10]++;
        	value = value/10;
        }
        for(int result : aa) {
        	System.out.println(result);
        }
    }
    
}
