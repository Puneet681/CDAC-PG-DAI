import java.util.Scanner;

public class If_else {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter New Input : ");
		int check = sc.nextInt();
		
		if(check%2==0)
			System.out.println("Even...");
		else
			System.out.println("Odd...");
		
		System.out.println("Using For Loop : ");
		for(int i=1 ; i<=10 ; i++) {
			System.out.print(i*check+" ");
		}
		
		System.out.println("Using For Loop");
		int  i = 1;
		while(i<=10) {
			System.out.print(i*check+" ");
			i++;
			
		sc.close();
		}

	}

}
