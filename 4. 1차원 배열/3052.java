import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int aa[] = new int[42];
        int count = 0;
        
        for(int i=0; i<10; i++) {
        	int N = Integer.parseInt(br.readLine());
        	int nam = N%42;
        	aa[nam]++; 
        }
        for(int i=0; i<42; i++) {
        	if(aa[i]>0) {
        		count++;
        	}
        }
        System.out.println(count);
    }
}
