import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
      
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        
        int index = 0;
        int aa[] = new int[N];
        
        while(st.hasMoreTokens()) {
        	aa[index] = Integer.parseInt(st.nextToken());
        	index++;
        }
        Arrays.sort(aa);
        System.out.print(aa[0]+" "+aa[N-1]);
       
    }
}
