import java.util.Scanner;
public class Main {

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
	
		int H = sc.nextInt();
		int M = sc.nextInt();
		int P = sc.nextInt();
		
		if((M+P>=60)&&((H+((M+P)/60))<24))
			System.out.printf("%d %d",H+((M+P)/60),(M+P)%60);
		else
			if((M+P>=60)&&((H+((M+P)/60))>=24))
			System.out.printf("%d %d",H+((M+P)/60)-24,(M+P)%60);
			else
				if(M+P<60)
				System.out.printf("%d %d",H, M+P);
			sc.close();
		
	}

}
