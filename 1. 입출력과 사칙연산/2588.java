import java.util.Scanner;
public class Main {

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		int b=sc.nextInt();
		
		System.out.printf("%d\n",a*(b%10));
		System.out.printf("%d\n",a*((b%100)/10));
		System.out.printf("%d\n",a*(b/100));
		System.out.printf("%d\n",a*b);
		
	
		sc.close();
		
	}

}
