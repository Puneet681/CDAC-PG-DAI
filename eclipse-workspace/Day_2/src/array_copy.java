
public class array_copy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] a = {1,2,3,4,5};
		int [] b = new int[3];
		System.arraycopy(a, 2, b, 0, 3);
		
		for(int val:b) {
			System.out.print(val+" ");
		}
	}

}
