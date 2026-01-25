import java.util.Scanner;

public class Hello {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		for (int i = 1; i <= t; i++) {
			System.out.println("Case #" + i + ": Hello!");
		}
		if (System.getenv("DOMJUDGE") != null) {
			System.out.println("I'm a debug message");
		}
	}
}
