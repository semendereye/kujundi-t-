
public class ul16 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int summa = 0;
		int[] numbrid = {12, 5, 10, 10, 28, 17, 5, 19, 0, 13, 0, 22, 7, 0, 17, 2, 24, 1, 13, 29, 0, 7, 16, 8, 7, 4};
		for(int i : numbrid)
			summa += i;
		System.out.println("Summa: " + summa);
		int elemendid = numbrid.length;
		double kesk = ((double)summa) / elemendid;
		System.out.println("keskmine: " + kesk);
	}

}
