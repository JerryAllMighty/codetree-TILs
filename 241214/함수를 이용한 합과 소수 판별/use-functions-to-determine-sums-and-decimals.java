import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    static boolean isPrime(int n) {
        boolean result = true;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return result;
    }

    static boolean isSumEven(int n) {
        boolean result = false;
        int totalSum = 0;
        String strN = Integer.toString(n);
        for (int i = 0; i < strN.length(); i++) {
            totalSum += Integer.parseInt(strN.substring(i,i+1));
        }
        if (totalSum % 2 == 0) {
            result = true;
        }
        return result;
    }

    static boolean isValid(int n) {
        boolean result = false;
        if (isPrime(n) && isSumEven(n)) {
            result = true;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int answer = 0;
        for (int i = a; i <= b; i++) {
            if (isValid(i)) {
                answer++;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}

