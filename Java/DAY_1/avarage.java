import java.util.Scanner;

public class avarage {

	public static void main(String[] args) {
		int a,b,c,d,e;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter 5 Numbers");
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt(); d = sc.nextInt();
		e = sc.nextInt();
		
		float avg = (a+b+c+d+e)/5.0f;
		
		System.out.println("Avrage = "+avg);
	}

}


// cltr+space => auto-complete
// cltr+click =. jumping to defination