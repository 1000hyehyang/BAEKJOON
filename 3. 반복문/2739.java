import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a;
        int b = sc.nextInt();
        
        for(a=1; a<=9; a++){
        	System.out.printf("%d * %d = %d\n",b,a,b*a);
        sc.close();
        }
    }
}
