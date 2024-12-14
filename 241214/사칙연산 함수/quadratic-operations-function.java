import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int a = sc.nextInt();
            String o = sc.next();
            int c = sc.nextInt();
            String answer = "";
            switch (o) {
                case "+":
                    answer = String.valueOf(a + c);
                    break;
                case "-":
                    answer = String.valueOf(a - c);
                    break;
                case "/":
                    answer = String.valueOf(a / c);
                    break;
                case "*":
                    answer = String.valueOf(a * c);
                    break;
                default:
                    throw new InputMismatchException("False");
            }

            System.out.println(Integer.toString(a) + " " + o + " " + Integer.toString(c) + " " + "= " + answer);
        } catch (InputMismatchException e) {
            System.out.println("False");
        }


    }
}

