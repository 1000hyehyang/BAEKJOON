import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          
        int N = Integer.parseInt(br.readLine());
        String ox[] =  new String[N];
        
        for(int i=0; i<N; i++) {
        	ox[i] = br.readLine();
        }
        for(int i=0; i<N; i++) {
        	int count = 0;
        	int sum = 0;
        	
        	for(int j=0; j<ox[i].length(); j++) {
        		if(ox[i].charAt(j)=='O') {
        			count++;
        			sum = sum + count;
        		}else {
        			count = 0;
        		}      		
        	}
        	System.out.println(sum);
        }
    }
}
