import java.util.Scanner;

class AccountHolder{
	private int no;
	private String name;
	private int balance;
	
	
	//Parameterized Constructor 
	public AccountHolder(int no, String name, int balance) {
		this.no = no;
		this.name = name;
		this.balance = balance;
	}

	public AccountHolder() {
		no = 0;
		name = "None";
		balance = 0;
	}
	
	public int getNo() {
		return no;
	}

	public void setNo(int no) {
		this.no = no;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		this.balance = balance;
	}
	
	public int deposit(int bal) {
		this.balance = this.balance + bal;
		return this.balance;
	}
	
	
	public int withdraw(int bal) {
		this.balance = this.balance - bal;
		return this.balance;
	}

	public String toString() {
		return "no=" + no + ", name=" + name + ", balance=" + balance;
	}
	
}


public class A2Q1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cnt = 0;
		AccountHolder [] arr = new AccountHolder[10];
		
		while(true)
		{
		
			System.out.println("1. Add record for account holder\n"
					+ "2. Display details of all account holders.\n"
					+ "3. Deposite an amount into perticular account\n"
					+ "4. Withdraw an amount from perticular account\n"
					+ "5. Exit");
			int expr = sc.nextInt();
			
			if(expr==5) {
				System.out.println("Thank you for visiting...");
				break;
			}
			
			switch(expr) {
			
			case 1:
				
				System.out.println("1.Enter Acc No\n"
						+"2.Name\n"
						+"3.Balance");
	 			AccountHolder Ac = new AccountHolder(sc.nextInt(),sc.next(),sc.nextInt());
	 			
	 			arr[cnt++] = Ac;
	 			break;
	 			
			case 2:
				for(int i=0;i<cnt;i++) {
					System.out.println(arr[i]);
				}
				break;
			
			case 3:	
				
				
				System.out.println("Enter Acc No : ");
				int ACCno = sc.nextInt();
			
				for(int i=0;i<cnt;i++) {
					if(arr[i].getNo() == ACCno) {
						System.out.println("Enter Deposit Amount : ");
						System.out.println("New Amount : "+arr[i].deposit(sc.nextInt()));
					}
				}
				break;
	 
				
			case 4:
				
				
				System.out.println("Enter Acc No : ");
				ACCno = sc.nextInt();
				
				for(int i=0;i<cnt;i++) {
					if(arr[i].getNo() == ACCno) {
						System.out.println("Enter Withdrwal Amount : ");
						System.out.println("Remaining Amount : "+arr[i].withdraw(sc.nextInt()));
					}
				}
				break;
			}
			
			
		}

		}
		
}
