import java.util.Scanner;
public class Main {

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		
		int H = sc.nextInt();
		int M = sc.nextInt();
		
		
		if((M-45<0)&&(H!=0))
			System.out.printf("%d %d",H-1,M+15);
		else
			if((M-45<0)&&(H==0))
			System.out.printf("%d %d",H+23,M+15);
			else
				if(M-45>=0)
				System.out.printf("%d %d",H, M-45);
			sc.close();
		
	}

}
