import java.util.Scanner;

class Tester 
{
	public static void main(String [] args)
	{
		int a, b;
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter two Numbers");
		a = sc.nextInt();
		b = sc.nextInt();
		
		int c=a+b;
		
		System.out.println("Sum = "+c);
				
		
	}
}

// Write a program to claculate avrage of five user enterd integers.


class Avarage
{
	public void ans(String [] args)
	{
		int a,b,c,d,e;
		System.out.println("Enter five numbers:");
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		d = sc.nextInt();
		e = sc.nextInt();
		
		int ans = (a+b+c+d+e)/5;
		
		System.out.println("Avrage is ="+ans);
	}
	

}
