import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    static boolean isComplete(int n) {
        boolean result = true;
        if (n % 2 == 0) {
            result = false;
        }
        String strN = Integer.toString(n);
        if (strN.charAt(strN.length() - 1) == '5') {
            result = false;
        }
        if (n % 3 == 0 && n % 9 != 0) {
            result = false;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int answer = 0;
        for (int i = a; i <= b; i++) {
            if (isComplete(i)) {
                answer++;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}

