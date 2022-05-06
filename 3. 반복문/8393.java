import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       
        int a = 0;
        int i;
        int n = sc.nextInt();
      
        for(i=1; i<=n; i++) {
         a = a + i;
        }
        System.out.printf("%d",a);
        sc.close();
     
    }
}
